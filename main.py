import pymupdf
import pandas as pd

doc = pymupdf.open("語彙表－大地1  L3.pdf")
tabs = doc[0].find_tables()

if tabs.tables: 
   tab = tabs[0].to_pandas()
   tab = tab.drop(columns=["課", "Col1", "Col2", "品詞"])
   tab = tab.loc[~(tab == "").all(axis=1)]
   tab.columns = ["romaji", "hiragana/katakana", "kanji", "portuguese"]
   tab.to_csv("output.csv")
   