from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Labelview")

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
