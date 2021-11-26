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

    response = client.get()

    computers = response['data'] if response['success'] else []

    return render_template('index.html', employees = db_employees, computers = computers)


@app.route('/submit_new_computer', methods=['POST'])
def submit_new_computer():

    response = client.post(request.form)

    if not response['success']:
        return render_template('/error.html')
        
    return render_template('submit_new_computer.html', employee = request.form['employee'], computers = response['data'])


@app.route('/get_computers', methods=['POST'])
def get_computers():

    response = client.get(request.form['employee'])

    if not response['success']:
        return render_template('/error.html')
        
    return render_template('get_computers.html', employee = request.form['employee'], computers = response['data'])


@app.route('/remove_computer', methods=['POST'])
def remove_computer():

    computer_id = request.form['computer']

    response = client.get_by_id(computer_id)

    if not response['success']:
        return render_template('/error.html')

    computer = response['data']
    employee = computer['employee']
    computer['employee'] = ''

    putresponse = client.put(computer['id'], computer)

    if not putresponse['success']:
        return render_template('/error.html')

    return render_template('remove_computer.html', computer = computer['name'], employee = employee)


@app.route('/reassign_computer', methods=['POST'])
def reassign_computer():

    computer_id = request.form['computer']

    response = client.get_by_id(computer_id)

    if not response['success']:
        return render_template('/error.html')

    computer = response['data']
    computer['employee'] = request.form['employee']

    putresponse = client.put(computer['id'], computer)

    if not putresponse['success']:
        return render_template('/error.html')

    return render_template('reassign_computer.html', computer = computer['name'], employee = request.form['employee'])