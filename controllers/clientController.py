from flask import Blueprint, request, jsonify
from .databaseClient import DatabaseClient
from .AzureBlobStorageClient import AzureBlobStorageClient

bp = Blueprint('main', __name__)

# Initialize database and storage clients
db_client = DatabaseClient()
blob_client = AzureBlobStorageClient()

@bp.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    client_id = db_client.create_client(data)
    blob_client.create_container(client_id)
    return jsonify({'client_id': client_id}), 201

@bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = db_client.get_client(client_id)
    if client:
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    updated = db_client.update_client(client_id, data)
    if updated:
        return jsonify({'message': 'Client updated'}), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    deleted = db_client.delete_client(client_id)
    if deleted:
        blob_client.delete_container(client_id)
        return jsonify({'message': 'Client deleted'}), 200
    else:
        return jsonify({'error': 'Client not found'}), 404



