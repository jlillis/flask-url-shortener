# IT-229-A Project 2 Journal

## 11/25/2019 - Project Initialization
I started work on the project by setting up the development environment:
* Created a project folder with basic git dotfiles, LICENSE.txt, README.md, and JOURNAL.md
* Created a python virtual environment (venv) with the commmand `python -m venv venv`
    * From now on, work on this project (including module installation) will take place within this venv
    * To activate (on Windows): `.\venv\Scripts\activate`
    * To deactivate: `deactivate`
* Defined python module requirements in `requirements.txt`
    * The only require python module as of now is `Flask`
    * Required packages can be installed with `pip install -r requirements.txt`
* Copy & pasted the [Flask "Hello, World!" example](https://flask.palletsprojects.com/en/1.1.x/quickstart/) into app.py
* Tested the environment by running `flask run`
* Initialized the project folder as a git repository, and pushed the project to GitHub

## 11/26/2019 - First Steps
### python-dotenv setup
I decided to use python-dotenv to setup environment variables automatically rather than having to set them via command line all the time. I followed the [instructions from the Flask docs](https://flask.palletsprojects.com/en/1.1.x/cli/#dotenv):
1. Added the `python-dotenv` package to `requirements.txt`
2. Ran `pip install -r requirements.txt` to update installed packages.
4. Added `.env` to set `FLASK_ENV=development`
    * Note: `.env` is environment-specific and is excluded from the repo in `.gitignore`

### Template rendering
Flask uses the [Jinja template engine](https://palletsprojects.com/p/jinja/) to render HTML templates, which makes building the app's webpages easy. Templates for the app are defined in the `templates/` directory. The `base.html` template includes the [Bootstrap CSS library](https://getbootstrap.com/) which will be used later to make styling quick and easy. The templates for each page will inherit the base template and in turn the bootstrap library.

### Reading and validating user input
To read user input the view function must be setup to accept POST requests:
```
@app.route('/', methods=("GET", "POST"))
```
When a POST request is recieved, Flask will pass a [`Request` object](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request) to the view function that can be used to read POST data. To validate the URL, I choose to use the url validator from the [validators](https://validators.readthedocs.io/en/latest/#) package.

### URL redirects, part 1
For the first implementation of URL redirects, I chose to use the first 6 characters of the md5 hash (hexadecimal) as the short URL. I store the records in a dictionary during runtime only. There are two problems with this:
1. The short URLs are not unique enough - a better method for generating short URLs is needed
2. All links are lost when the web server restarts - they need to be saved in a database

There should probably also be some sort of redirect page with a countdown timer, as well as a listing of all shortened URLs for managment purposes.