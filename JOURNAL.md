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