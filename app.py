from flask import Flask, render_template, request


def create_app():
    
    app = Flask(__name__)

    return app


app = create_app()


@app.route('/')
def index():

    return render_template('index.html')