import argparse
from pdf_reader import pdf_reader

parser = argparse.ArgumentParser()

parser.add_argument("PDFfilename")

args = parser.parse_args()

pdf_reader(args.PDFfilename)