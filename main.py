import pymupdf
import pandas as pd
from google import genai
import os
import ast
import argparse
from pathlib import Path

def kanji_to_furigana():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

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

   chat = client.chats.create(model="gemini-2.0-flash-lite-preview-02-05")

   response = chat.send_message(
      message=prompt
   )

   response = chat.send_message(
      message=repr(kanji_list)
   )

   return response.text

parser = argparse.ArgumentParser()

parser.add_argument("PDFfilename")
parser.add_argument("-o", "--OCR", action="store_true")
   
args = parser.parse_args()

doc = pymupdf.open(args.PDFfilename)

if args.OCR:
   print("option not yet implemented")
   raise SystemExit(1)

tabs = doc[0].find_tables()

if tabs.tables: 
   tab = tabs[0].to_pandas()
   tab = tab.drop(columns=["課", "Col1", "Col2", "品詞"])
   tab = tab.loc[~(tab == "").all(axis=1)]
   tab.columns = ["romaji", "hiragana-katakana", "kanji", "portuguese"]

   kanji_list = tab["kanji"].tolist()

   furigana_list = kanji_to_furigana()
   furigana_list = furigana_list.strip("```\n")

   tab["hiragana-katakana"] = [
      furigana if furigana != '' else katakana_hiragana 
      for katakana_hiragana, furigana in zip(tab["hiragana-katakana"], ast.literal_eval(furigana_list))
   ]

   tab = tab.rename(columns={"hiragana-katakana": "hiragana-katakana-furigana"})
   tab = tab.drop(columns="kanji")

   tab.to_csv(str(Path(args.PDFfilename).with_suffix(".csv")))