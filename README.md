# flask-url-shortener

This is a basic URL shortener web app built using Flask.


## Getting Started

### Installation
1. If downloaded as a .zip, unzip the project files
2. To install the required packages, just run the following command in the main project folder:
```
pip install -r requirements.txt
```
3. To initialize the database, run the following commands:
```
flask db init
flask db migrate
flask db upgrade
```
4. To run the web server, run `flask run`