from flask import Blueprint, request, jsonify
from controllers.ContractController import ContractController
from controllers.ClientController import ClientController

contract_controller = Blueprint('contract_blueprint', __name__)
contract_controller = ContractController()
client_controller = ClientController()

@contract_controller.route('/contracts', methods=['GET'])
def get_contracts():
    return jsonify(contract_controller.get_contracts())

@contract_controller.route('/contracts/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    return jsonify(contract_controller.get_contracts(contract_id))

@contract_controller.route('/contracts', methods=['POST'])
def create_contract():
    client_id = request.json.get('client_id')
    # validate client_id
    client = client_controller.get_client(client_id)

    # upload contract file
    file = request.files['file']
    filename =  "contracts/"+file.filename
    contract_controller.upload_contract_file(file, filename)

    contract_name = request.json.get('contract_name')
    contract_document_link = request.json.get('contract_document_link')

    contract_id = contract_controller.create_contract(request.json)
    return jsonify({'id': contract_id}), 201

@contract_controller.route('/contracts/<int:contract_id>', methods=['PUT'])
def update_contract(contract_id):
    contract_controller.update_contract(contract_id, request.json)
    return jsonify({'message': 'Contract updated successfully'})

@contract_controller.route('/contracts/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    contract_controller.delete_contract(contract_id)
    return jsonify({'message': 'Contract deleted successfully'})

@contract_controller.route('/contracts/upload', methods=['POST'])
def upload_contract_file():
    file = request.files['file']
    if file:
        blob_url = contract_controller.upload_contract_file(file)
        return jsonify({'url': blob_url}), 201
    return jsonify({'message': 'No file attched'}), 400