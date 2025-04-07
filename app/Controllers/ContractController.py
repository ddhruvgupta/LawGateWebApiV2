from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models import Contract, Client  # assumes you have a Client model too
import os

contract_bp = Blueprint('contract_blueprint', __name__)

@contract_bp.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    results = [contract.to_dict() for contract in contracts]  # assumes to_dict() defined in model
    return jsonify(results)

@contract_bp.route('/contracts/<int:contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)
    return jsonify(contract.to_dict())

@contract_bp.route('/contracts', methods=['POST'])
def create_contract():
    data = request.get_json() or {}
    client_id = data.get('client_id')
    if not client_id:
        return jsonify({'message': 'client_id is required'}), 400

    # Ensure the client exists
    client = Client.query.get(client_id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404

    # upload contract file if provided
    file = request.files.get('file')
    filename = None
    if file:
        filename = os.path.join("contracts", file.filename)
        upload_path = os.path.join(current_app.config.get('UPLOAD_FOLDER', ''), filename)
        file.save(upload_path)

    # create a new contract record
    contract = Contract(
        client_id=client_id,
        contract_name=data.get('contract_name'),
        contract_document_link=data.get('contract_document_link') or filename
    )
    db.session.add(contract)
    db.session.commit()

    return jsonify({'id': contract.id}), 201

@contract_bp.route('/contracts/<int:contract_id>', methods=['PUT'])
def update_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)
    data = request.get_json() or {}

    # update fields; add checks as needed
    contract.contract_name = data.get('contract_name', contract.contract_name)
    contract.contract_document_link = data.get('contract_document_link', contract.contract_document_link)

    # Update client if provided and exists
    if 'client_id' in data:
        client = Client.query.get(data['client_id'])
        if not client:
            return jsonify({'message': 'Client not found'}), 404
        contract.client_id = data['client_id']

    db.session.commit()
    return jsonify({'message': 'Contract updated successfully'})

@contract_bp.route('/contracts/<int:contract_id>', methods=['DELETE'])
def delete_contract(contract_id):
    contract = Contract.query.get_or_404(contract_id)
    db.session.delete(contract)
    db.session.commit()
    return jsonify({'message': 'Contract deleted successfully'})

@contract_bp.route('/contracts/upload', methods=['POST'])
def upload_contract_file():
    file = request.files.get('file')
    if file:
        filename = os.path.join("contracts", file.filename)
        upload_path = os.path.join(current_app.config.get('UPLOAD_FOLDER', ''), filename)
        file.save(upload_path)
        # For example, return the URL of the uploaded file:
        blob_url = f"/uploads/{filename}"
        return jsonify({'url': blob_url}), 201
    return jsonify({'message': 'No file attached'}), 400