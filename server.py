from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['GET', 'POST'])
def englishToFrench():
    english_sentence = request.args.get('textToTranslate')
    return translator.english_to_french(english_sentence)

@app.route("/frenchToEnglish", methods=['GET', 'POST'])
def frenchToEnglish():
    french_sentence = request.args.get('textToTranslate')
    return translator.french_to_english(french_sentence)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
   # with  open('./templates/index.html') as f:
      #  return f.read()

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)

