import pymupdf
import pandas as pd
import google.generativeai as genai
import os
import ast

def kanji_to_furigana():
   genai.configure(api_key=os.environ["GEMINI_API_KEY"])

   prompt = """I want you to act as a Japanese language teacher.
               I will send you a list of words written in kanji, and you must
               convert them by adding their corresponding hiragana readings.
               
               Each individual kanji in a compound word must be followed by its
               most commonly used hiragana reading in brackets. For example:
               携帯電話 → 携[けい]帯[たい]電[でん]話[わ] (correct)
               携帯電話[けいたいでんわ] (incorrect, do not use full word furigana)
               
               Important rules:
               - Use the most common reading for each kanji in compound words 
               (prioritizing on’yomi unless the word usually takes kun’yomi).
               - Do not modify non-kanji characters (hiragana, katakana, 
               punctuation, and numbers must remain unchanged).
               - Words that begin with katakana but contain kanji must also be
               processed. For example:
               ゲーム機 → ゲーム機[き] (correct)
               ゲーム機 (incorrect, do not ignore the kanji just because the word
               starts with katakana)
               - The output must preserve the original structure and order of
               the input, modifying only the kanji that require furigana"""


   generation_config = {
   "temperature": 0.2,
   "top_p": 0.95,
   "top_k": 64,
   "max_output_tokens": 8192,
   "response_mime_type": "text/plain",
   }

   model = genai.GenerativeModel(
   model_name="gemini-2.0-flash-lite-preview-02-05",
   generation_config=generation_config,
   system_instruction=prompt,
   )

   response = model.start_chat().send_message(repr(kanji_list))

   return eval(response.text)

doc = pymupdf.open("語彙表－大地1  L3.pdf")
tabs = doc[0].find_tables()

if tabs.tables: 
   tab = tabs[0].to_pandas()
   tab = tab.drop(columns=["課", "Col1", "Col2", "品詞"])
   tab = tab.loc[~(tab == "").all(axis=1)]
   tab.columns = ["romaji", "hiragana/katakana/furigana", "kanji", "portuguese"]

   kanji_list = tab["kanji"].tolist()
   furigana_dict = kanji_to_furigana()

   tab["kanji"] = tab["kanji"].map(furigana_dict)

   tab.to_csv("output.csv")