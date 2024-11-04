from flask import Flask, render_template
import requests
from googletrans import Translator

app = Flask(__name__)


def fetch_quote():
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return {'content': 'Could not retrieve quote', 'author': ''}


def translate_quote_to_russian(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='ru')
    return translation.text


@app.route('/')
def index():
    quote = fetch_quote()
    translated_text = translate_quote_to_russian(quote['content'])
    quote['translation'] = translated_text
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True)
