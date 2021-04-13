import os
import gspread

from flask import Flask
import os.path
from flask import render_template, request, jsonify, abort
from oauth2client.service_account import ServiceAccountCredentials


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
        legal = request.args.get('legal')
        budget = request.args.get('budget')
        # We have our query string nicely serialized as a Python dictionary
        args = request.args
        animals = args.getlist("animal")
        produce = args.getlist("produce")
        governance = args.getlist("governance")

        # We'll create a string to display the parameters & values
        serialized = ", ".join(f"{k}: {v}" for k, v in request.args.items())

        # Display the query string to the client in a different format
        # return f"(Query) {serialized}  {animals}", 200
        hh = data.get_all_values()
        
        return render_template('result.html', page_title="Labelview", budget=hh, legal=legal, animal=animals, produce=produce, governance=governance )
    else:

        return "No query string received", 200 





# @app.route('/result', methods=['POST'])
# def result():
#     try:
#         legal = request.form.get('legal')
#         budget = request.form.get('budget')

#         sql_insert = """
#         INSERT INTO UserInput (legal, budget) VALUES (\"{legal}\",\"{budget}\");
#         """.format(
#             legal=legal, budget=budget)

#         # connect to the database with the filename configured above
#         # returning a 2-tuple that contains a connection and cursor object
#         # --> see file database_helpers for more
#         database_tuple = connect_to_database(app.config['labelview/data/labelview.sqlite'])

#         # now that we have connected, add the new meeting (insert a row)
#         # --> see file database_helpers for more
#         change_database(database_tuple[0], database_tuple[1], sql_insert)

#         # now, get all of the meetings from the database, not just the new one.
#         # first, define the query to get all meetings:
#         sql_query = "SELECT * FROM UserInput;"


#         # query the database, by passinng the database cursor and query,
#         # we expect a list of tuples corresponding to all rows in the database
#         query_response = query_database(database_tuple[1], sql_query)
#         close_conection_to_database(database_tuple[0])

#         # In addition to HTML, we will respond with an HTTP Status code
#         # The status code 201 means "created": a row was added to the database
#         return render_template('result.html', page_title="Result",
#                                result=query_response, ), 201

#     except Exception:
#         # something bad happended. Return an error page and a 500 error
#         error_code = 500
#         return render_template('error.html', page_title=error_code), error_code


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
