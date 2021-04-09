# Flask Website Starter Template 

- Activate your virtual environment for this project: 
   
    macOS/Linux: `source venv/bin/activate`


- Point Flask to your application:  

    macOS/Linux:  `export FLASK_APP=main.py`

- Enable hot reloading, debug mode, and other useful features for local development:  

     macOS/Linux: `export FLASK_APP=main.py`

- run your flask application: 

    `flask run`

## While You're Developing... 

To test your app: 

> pytest --doctest-modules

To Lint your app: 
> flake8 --exclude venv 



### Get Set Up for Local Development: 
    
    > python3.8 -m venv venv 
    > pip install -r requirements.txt
    > uwsgi --http-socket 127.0.0.1:5000 --wsgi-file labelview/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/





At this stage, your website should be running on the internet, live! 

## Make This Repository Your Own

Now that you have verified that this setup works, it is time to make it your own. Here are a few things I suggest changing right away:   
- The repository name, if you haven't yet. 
- Change the title of the index page
- Edit the CSS a little, changing a font or color.
- Rename the folder `labelview` to be your project name. When you do this, you will have to change a few references to the directory: in `app.yaml`, `main.py`, and `test_labelview.py`. You can use the feature `Edit --> Find in Files` to find all occurrences of the name to make sure you have found them all. 

Even before you add any "features", this makes the website and code look and feel more like it is yours already! 

Once you have made some of these small changes, remember to add, commit, and push your changes - and with that, it should automatically be live on the internet! 


Hopefully only I will see this change...