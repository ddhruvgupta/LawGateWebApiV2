'''Client controller is responsible for adding new clients, updating client information, 
deleting clients and getting client information'''

import uuid
from flask import Blueprint, request, jsonify
from clients.databaseClient import DatabaseClient
from clients.AzureBlobStorageClient import AzureBlobStorageClient
from models.clientModel import ClientModel, Client
import re

client_blueprint = Blueprint('client_blueprint', __name__)

# Initialize database and storage clients
cm = ClientModel(DatabaseClient())
blob_connection_string = "DefaultEndpointsProtocol=https;AccountName=csg10032000b0467fa5;AccountKey=M1S5aSIHJlPjf+bpmEbSvt/7U2J70r3bzz0xFElrYmm0P8UqU94CzT6DCp+ppDSuWbg4kf0058Kn+AStabE/fw==;EndpointSuffix=core.windows.net"
blob_client = AzureBlobStorageClient(blob_connection_string)

@client_blueprint.route('/clients', methods=['POST'])
def create_client():
    #TODO validate data
    print(request.json)
    blob_container_name = str(uuid.uuid4())

    isContainerCreated = blob_client.create_container(blob_container_name)
    if isContainerCreated:
        client = Client()
        client.populate(request.json)
        client.blob_storage_container_name = blob_container_name
        try:
            data = cm.create_client(client)
        except Exception as e:
            blob_client.delete_container(blob_container_name)
            return jsonify({'Error': "Unable to add Client"}), 501

    
    return jsonify({'client_id': data}), 201

@client_blueprint.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    
    clnt = cm.read_client(client_id)
    if clnt:
        return jsonify(clnt), 200
    else:
        return jsonify({'error': 'Client not found'}), 404
    
@client_blueprint.route('/clients/', methods=['GET'])
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
        _ = cm.update_client(client_id, data)
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
    

def validate_client_data(data):
    pass
    #TODO validate data
    required_fields = ['client_name', 'client_email', 'client_phone']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, data['client_email']):
        return False, "Invalid email address"
    
    phone_regex = r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$'
    if not re.match(phone_regex, data['client_phone']):
        return False, "Invalid phone number"
    
    return True
