from flask import Flask, render_template, jsonify, request
from random import *
from flask_restful import Resource, Api, reqparse, abort
import os
import pandas as pd


app = Flask(__name__)

UPLOAD_FOLDER = '/Users/andersketelsen/Desktop/Kodning/Vue/uploads'
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER

filepath = ""

def getAttributeNames():
    data=pd.read_csv('uploads/train.csv')
    return jsonify(data.columns.values.tolist())
#Basic post og get metoder til samme URL
# Post metoden henter fra json body som sendes via axios i frontend
@app.route('/', methods=['GET','POST'])
def random_number():
    if request.method == "POST":
        response = request.get_json()['body']
        return response
    elif request.method == "GET":
        return "Du har gettet"

# Helt simpel fil upload uden error handling osv. 
@app.route('/fileupload', methods=['POST'])
def fileUpload():
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    return getAttributeNames()


if __name__ == '__main__':
    app.run(debug=True)




