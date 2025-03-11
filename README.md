# AnkiVocabExtractor JP

This project converts PDF file to CSV file for use in creating Anki Decks. It's a very specific project I did to create flashcards from the vocabulary lists I received from the Japanese course I took.

I also implemented a kanji to furigana converter in Anki format using the Google Gen AI SDK.

## Installation

Because of the Google Gen AI SDK, you need a Gemini API key which you can get at <https://aistudio.google.com/app/apikey>.

To install the required dependencies, first, create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

To run the project, provide a PDF file as an argument:

```bash
python3 main.py file_name.pdf
```

Replace `file_name.pdf` with the actual name of your PDF file.