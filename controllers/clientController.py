from flask import Blueprint, request, jsonify
from Services.ClientController import ClientController
from helpers.ClientDataValidator import ClientDataValidator

# Load environment variables from .env file
client_blueprint = Blueprint('client_blueprint', __name__)
client_controller = ClientController()

@client_blueprint.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    is_valid, message = ClientDataValidator.validate_all_required_fields(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    response = client_controller.create_client(data)
    if response:
        return jsonify(response), 201
    else:
        return jsonify({'error': 'Client not created'}), 500


@client_blueprint.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = client_controller.get_client(client_id)
    if client:
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@client_blueprint.route('/clients/', methods=['GET'])
def get_all_clients():
    clients = client_controller.get_all_clients()
    if clients:
        return jsonify(clients), 200
    else:
        return jsonify({'error': 'Clients not found'}), 404

@client_blueprint.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    is_valid, message = ClientDataValidator.validate_all(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    if get_client(client_id).status_code == 200:
        client_controller.update_client(client_id, data)
        return jsonify({'message': 'Client updated'}), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@client_blueprint.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        client_controller.delete_client(client_id)
        return jsonify({'message': 'Client deleted'}), 200
    except Exception as e:
        return jsonify({'error': 'Client not found'}), 404