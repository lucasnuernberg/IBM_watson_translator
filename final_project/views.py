import json
import machinetranslation
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    return machinetranslation.englishTofrench(textToTranslate)

@views.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return machinetranslation.frenchToEnglish(textToTranslate)

@views.route("/")
def renderIndexPage():

    return render_template('index.html')

# Write the code to render template