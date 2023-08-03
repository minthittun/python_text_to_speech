import os
import base64
from flask import Flask, request, jsonify, render_template
from gtts import gTTS
from googletrans import Translator




app = Flask(__name__, static_folder='static')

# Function to detect the language of the given text
def detect_language(text):
    translator = Translator()
    detected_lang = translator.detect(text).lang
    return detected_lang


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/texttospeech', methods=['POST'])
def text_to_speech():
    # Get the text from the request body
    data = request.json
    text = data.get('text', '')
    words = text.split(' ')
    
    with open('output.mp3', 'wb') as ff:
        for word in words:
            # Detect the language of the text
            detected_language = detect_language(word)
            gTTS(text=word, lang=detected_language, slow=False).write_to_fp(ff)
    
    # Read the temporary file and convert it to base64
    with open("output.mp3", 'rb') as file:
        audio_bytes = file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()


    # Return the audio content as base64 encoded string
    return jsonify({'audio_base64': audio_base64})

if __name__ == '__main__':
    app.run(debug=True)
