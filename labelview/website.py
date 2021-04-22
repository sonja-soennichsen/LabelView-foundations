import os
import gspread

from flask import Flask
import os.path
from flask import render_template, request
from oauth2client.service_account import ServiceAccountCredentials
from labelview.controllers.helperFunction import findAllLabels


app = Flask(__name__)
# configure Flask using environment variables
app.config.from_pyfile("config.py")


if os.path.isfile('/Users/ssoennic/LabelView/Labelview-foundations/credentials.json'):
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/ssoennic/LabelView/Labelview-foundations/credentials.json',
                                                                    ["https://spreadsheets.google.com/feeds", 
                                                                    "https://www.googleapis.com/auth/spreadsheets", 
                                                                    "https://www.googleapis.com/auth/drive.file", 
                                                                    "https://www.googleapis.com/auth/drive"])
else:
    credentials = ServiceAccountCredentials.from_json_keyfile_name('./credentials.json',
                                                                    ["https://spreadsheets.google.com/feeds", 
                                                                    "https://www.googleapis.com/auth/spreadsheets", 
                                                                    "https://www.googleapis.com/auth/drive.file", 
                                                                    "https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credentials)
spr = client.open("ecolabels")
data = spr.worksheet('ecolabelData')

@app.route('/')
def index():
    return render_template('index.html', page_title="Labelview")

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route("/result", methods=["GET"])
def result():
    if request.args:
        # get Form Input
        args = request.args
        legal = request.args.get('legal')
        budget = request.args.get('budget')
        animals = args.getlist("animal")
        produce = args.getlist("produce")
        governance = args.getlist("governance")

        # get Database
        database = data.get_all_values()
        
        # Search in Database for Labels
        labels_keywords = findAllLabels(database, budget, legal, produce, animals, governance)
        
        return render_template('result.html', page_title="Labelview",data=database, found=labels_keywords[0], bestLabel=labels_keywords[1]  )
    else:
        return render_template('error.html', page_title="Labelview")

@app.route('/overview')
def overview():
    database = data.get_all_values()
    return render_template('overview.html', data=database)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    database = data.get_all_values()
    return render_template('resources.html', data=database)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

