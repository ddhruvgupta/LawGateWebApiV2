'''Client controller is responsible for adding new clients, updating client information, 
deleting clients and getting client information'''

from flask import Blueprint, request, jsonify
from clients.databaseClient import DatabaseClient
from clients.AzureBlobStorageClient import AzureBlobStorageClient
from models.clientModel import ClientModel

client_blueprint = Blueprint('client_blueprint', __name__)

# Initialize database and storage clients
cm = ClientModel(DatabaseClient())
blob_connection_string = "DefaultEndpointsProtocol=https;AccountName=csg10032000b0467fa5;AccountKey=M1S5aSIHJlPjf+bpmEbSvt/7U2J70r3bzz0xFElrYmm0P8UqU94CzT6DCp+ppDSuWbg4kf0058Kn+AStabE/fw==;EndpointSuffix=core.windows.net"
blob_client = AzureBlobStorageClient(blob_connection_string)

@client_blueprint.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    #TODO validate data
    client_id = cm.create_client(data)
    blob_client.create_container(client_id)
    return jsonify({'client_id': client_id}), 201

@client_blueprint.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    
    clnt = cm.read_client(client_id)
    if clnt:
        return jsonify(clnt), 200
    else:
        return jsonify({'error': 'Client not found'}), 404
    
# @client_blueprint.route('/clients/', methods=['GET'])
def get_all_client():
    result = cm.fetch_all_clients()

    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@client_blueprint.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    #TODO validate data
    if get_client(client_id):
        updated = cm.update_client(client_id, data)
        # TODO check if the client is updated
        return jsonify({'message': 'Client updated'}), 200
    else: 
        return jsonify({'error': 'Client not found'}), 404


@client_blueprint.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    #TODO check if client exists
    if not get_client(client_id): 
        return jsonify({'error': 'Client not found'}), 404
    
    deleted = cm.delete_client(client_id)
    if deleted:
        blob_client.delete_container(client_id)
        return jsonify({'message': 'Client deleted'}), 200
