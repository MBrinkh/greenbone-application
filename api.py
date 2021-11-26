from flask import Blueprint, request, jsonify


api_Blueprint = Blueprint('api', __name__)


# This should be done (especially the dirty 'max_id' part) with a real database, but its runtime persistent and easy this way.
# Real world conditions would call for a docker container running a database engine, with the database mounted as a volume
# Building on that, I would create a model with an ORM of choice and proceed from there
db_computers = [
    { 'id': 1, 'name': 'Computer1', 'employee': 'ABC', 'macAddress': '01:23:45:67:89:FF', 'ipAddress': '127.0.0.1', 'description': 'This is a test'},
    { 'id': 2, 'name': 'Computer2', 'employee': 'ABC', 'macAddress': '01:23:45:67:89:AB', 'ipAddress': '127.0.0.2', 'description': 'This is another test'},
    { 'id': 3, 'name': 'Computer3', 'employee': 'DEF', 'macAddress': '01:23:45:67:89:DE', 'ipAddress': '127.0.0.3', 'description': 'This is another test'}
]

max_id = 2


@api_Blueprint.route('/computer', methods=['GET'])
def api_computer_get():

    if request.args.get('employee'):
        return jsonify(list(filter(lambda computer: computer['employee'] == request.args.get('employee'), db_computers)))

    return jsonify(db_computers) 


@api_Blueprint.route('/computer/<int:id>', methods=['GET'])
def api_computer_get_id(id):

    computer = next(filter(lambda computer: computer['id'] == id, db_computers), None)

    if not computer:
        return 'Not found', 404
        
    return computer


@api_Blueprint.route('/computer', methods=['POST'])
def api_computer_post():

    global max_id
    max_id += 1

    computer = {
        'id': max_id,
        'name': request.form['name'],
        'employee': request.form['employee'],
        'macAddress': request.form['macaddress'],
        'ipAddress': request.form['ipaddress'],
        'description': request.form['description'] if request.form['description'] else '',
    }

    db_computers.append(computer)

    return computer, 201


@api_Blueprint.route('/computer/<int:id>', methods=['PUT'])
def api_computer_put(id):

    computer = next(filter(lambda computer: computer['id'] == id, db_computers), None)

    if not computer:
        return 'Not found', 404

    computer['name'] = request.form['name']
    computer['employee'] = request.form['employee']
    computer['macAddress'] = request.form['macAddress']
    computer['ipAddress'] = request.form['ipAddress']
    computer['description'] = request.form['description']
        
    return computer


@api_Blueprint.route('/computer/<int:id>', methods=['DELETE'])
def api_computer_delete(id):

    computer = next(filter(lambda computer: computer['id'] == id, db_computers), None)

    if not computer:
        return 'Not found', 404

    db_computers.remove(computer)

    #One could argue to perform the 3 computers / employee check here

    return computer