from flask import Flask, render_template, request
from api import api_Blueprint


def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(api_Blueprint, url_prefix='/api')

    return app


app = create_app()


@app.route('/')
def index():

    return render_template('index.html')