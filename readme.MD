# Flask Website Starter Template

- Activate your virtual environment for this project: `source venv/bin/activate`

- Point Flask to your application: `export FLASK_APP=main.py`

- Enable hot reloading, debug mode, and other useful features for local development:  `export FLASK_ENV=development`

- run your flask application: `flask run`

## While You're Developing...

To test your app: `pytest --doctest-modules`

To Lint your app: `flake8 --exclude venv`

### Get Set Up for Local Development:

`python3.8 -m venv venv`
`pip install -r requirements.txt`
`uwsgi --http-socket 127.0.0.1:5000 --wsgi-file labelview/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/`
