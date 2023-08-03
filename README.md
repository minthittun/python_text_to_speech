# Text-to-Speech Web App using Flask and gTTS

This is a simple web application that converts text into speech using the gTTS (Google Text-to-Speech) library. The app is built with Flask, a lightweight web framework for Python.

### Features
1) **Text-to-Speech Conversion:** The web app takes input text and converts it into speech using the gTTS (Google Text-to-Speech) library.
2) **Language Detection:** The app can automatically detect the language of the input text.
3) **Multiple Language Support:** The app can handle sentences containing words from different languages. To achieve this, the sentence is split into words, and each word is processed separately.
4) **gTTS Enhancement:** gTTS cannot directly convert text with multiple languages contained in a sentence. Therefore, the app takes the extra step of splitting the sentence into words and processing them individually to overcome this limitation.
5) **MP3 File Generation:** The individual speech clips for each word are combined into a single MP3 file.
6) **Response in audio_base64:** The final audio file is encoded as base64 data and sent as a response to the client.

### Installation

1) Clone this repository to your local machine:
```
git clone https://github.com/minthittun/python_text_to_speech.git
cd python_text_to_speech
```

2) Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
```

3) Install the required dependencies:
```
pip install -r requirements.txt
```

### How to Run
```
python app.py
```

### Usage
1) input the text you want to convert into speech into the provided text box on the web page.
2) Add spaces between words from different languages contained in the sentence. 
This will ensure that the language detection works accurately for each word.
3) Click the "Convert to Speech" button.
4) The app will process the input text, split it into words, and convert each word into speech.
5) Once the conversion is complete, the app will combine all the individual speech clips into a single MP3 file.
6) The final MP3 audio file will be presented to you, and you can listen to the speech directly on the web page.

By adding spaces between words from different languages, you help the app correctly identify the language of each word, leading to more accurate text-to-speech conversions.

Feel free to use this updated section in your Markdown document. If you have any further requests or need more assistance, just let me know!
