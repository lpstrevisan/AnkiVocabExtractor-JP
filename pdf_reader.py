import pymupdf
import pandas as pd
import ast
from pathlib import Path
from kanji_convert import kanji_to_furigana

def pdf_reader(PDFfilename):
    doc = pymupdf.open(PDFfilename)

    tabs = doc[0].find_tables()

    if tabs.tables: 
        tab = tabs[0].to_pandas()
        tab = tab.drop(columns=["課", "Col1", "Col2", "品詞"])
        tab = tab.loc[~(tab == "").all(axis=1)]
        tab.columns = ["romaji", "hiragana-katakana", "kanji", "portuguese"]

        kanji_list = tab["kanji"].tolist()

        furigana_list = kanji_to_furigana(kanji_list)
        furigana_list = furigana_list.strip("```\n")

        tab["hiragana-katakana"] = [
            furigana if furigana != '' else katakana_hiragana 
            for katakana_hiragana, furigana in zip(tab["hiragana-katakana"], ast.literal_eval(furigana_list))
        ]

        tab = tab.rename(columns={"hiragana-katakana": "hiragana-katakana-furigana"})
        tab = tab.drop(columns="kanji")

        tab.to_csv(str(Path(PDFfilename).with_suffix(".csv")))
    else:
        print("Not found tables")
        raise SystemExit(1)