from google import genai
import os

def kanji_to_furigana(kanji_list):
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

   prompt = """I want you to act as a Japanese language teacher.
               I will send you a list of words written in kanji, and you must
               convert them by adding their corresponding hiragana readings.
               
               Each individual kanji in a compound word must be followed by its
               most commonly used hiragana reading in brackets. For example:
               携帯電話 → 携[けい]帯[たい]電[でん]話[わ] (correct)
               携帯電話[けいたいでんわ] (incorrect, do not use full word furigana)

               Output format:
               - Only return the processed list of words with the correct
               furigana formatting.
               - Do not include explanations, introductions, or any additional
               text.
               
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
               the input, modifying only the kanji that require furigana
               - Do not attempt to transform or adapt the input into valid
               Python syntax if it does not originally follow Python syntax"""

   chat = client.chats.create(model="gemini-2.0-flash-lite-preview-02-05")

   response = chat.send_message(
      message=prompt
   )

   response = chat.send_message(
      message=repr(kanji_list)
   )

   return response.text
