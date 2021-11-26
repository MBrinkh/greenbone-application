from flask import Flask, render_template, request
from api import api_Blueprint
from api_client import Api_Client


def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(api_Blueprint, url_prefix='/api')

    return app


app = create_app()


# In a real world scenario this client would be injected via DI with the appropriate configuration
# in this small scale demo app we will stick with a local initialization
client = Api_Client('http://localhost:5000/api/computer')

#Should come from a rest api, for simplicity its just hardcoded into the app
db_employees = [
    { 'abbreviation': 'ABC' },
    { 'abbreviation': 'DEF' },
    { 'abbreviation': 'GBR' },
]


@app.route('/')
def index():

    return render_template('index.html')