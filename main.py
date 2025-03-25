import argparse
from pdf_reader import pdf_reader

parser = argparse.ArgumentParser()

parser.add_argument("pdf_filename")

args = parser.parse_args()

pdf_reader(args.pdf_filename)