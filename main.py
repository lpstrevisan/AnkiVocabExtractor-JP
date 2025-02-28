import argparse
from pdf_reader import pdf_reader

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--OCR", action="store_true")
parser.add_argument("filename")

args = parser.parse_args()

if args.OCR:
   print("option not yet implemented")
   raise SystemExit(1)
else:
   pdf_reader(args.filename)