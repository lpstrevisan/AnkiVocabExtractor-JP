# AnkiVocabExtractor JP

This project converts PDF file to CSV file for use in creating Anki Decks. It's a very specific project I did to create flashcards from the vocabulary lists I received from the Japanese course I took.

I also implemented a kanji to furigana converter in Anki format using the Google Gen AI SDK

## Installation

Because of the Google Gen AI SDK, you need a Gemini API key which you can get at <https://aistudio.google.com/app/apikey>

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

To run the project, provide a PDF file as an argument:

```bash
python3 main.py file_name.pdf
```

Replace `file_name.pdf` with the actual name of your PDF file.
