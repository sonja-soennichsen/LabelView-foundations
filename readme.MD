# Flask Website Starter Template

- Activate your virtual environment for this project: `source venv/bin/activate`

- Point Flask to your application: export FLASK_APP=main.py FLASK_ENV=development

- run your flask application: `flask run`

## While You're Developing...

To test your app: `pytest --doctest-modules`

To Lint your app: `flake8 --exclude venv`

### Get Set Up for Local Development:

`python3.8 -m venv venv`
`pip install -r requirements.txt`
`uwsgi --http-socket 127.0.0.1:5000 --wsgi-file labelview/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/`

## Every Time You Develop on Your Project

Every time you restart your computer or reopen VSCode, you'll have to do a few things. Instructions for macOS and Linux distributions assume you are using a Bash shell. Instructions for Windows assume you are using the Command Prompt. Instructions for other shells can be found online.

- Activate your virtual environment for this project:

  macOS/Linux: `source venv/bin/activate`

  Windows: `venv\Scripts\activate.bat`

- Point Flask to your application:

  macOS/Linux: `export FLASK_APP=main.py`

  Windows: `set FLASK_APP=main.py`

- Enable hot reloading, debug mode, and other useful features for local development:

  macOS/Linux: `export FLASK_ENV=development`

  Windows: `set FLASK_ENV=development`

- run your flask application:

  `flask run`

## While You're Developing...

Whenever you deploy your code, it will be automatically testing and linted by the GitHub Action. To have a quicker feedback loop and to make sure there are as few surprises as possible, run the same commands locally, too:

To test your app:

> pytest --doctest-modules

To Lint your app:

> flake8 --exclude venv

## Before you start...

You should have:

- Python 3.8.x installed on your computer
- Visual Studio Code (or another IDE of your choosing) installed on your computer
- A GitHub account
- A Google Cloud Platform account (with class credits)

### Get Set Up for Local Development:

- Create a virtual environment

  > python3.8 -m venv venv

- Activate your virtual environment
  macOS/Linux: `source venv/bin/activate`
  Windows: `venv\Scripts\activate.bat`

- Download the Python modules

  > pip install -r requirements.txt

- Run the local development server and make sure it all works. Instructions can be found at the top of this readme for using Flask's built in development server. Alternatively (only on macOS or Linux), you can use the command `uwsgi` to start your development server:

> uwsgi --http-socket 127.0.0.1:5000 --wsgi-file great_project/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/
