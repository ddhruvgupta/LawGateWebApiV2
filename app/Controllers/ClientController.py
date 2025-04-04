from flask import Blueprint, abort, request, jsonify
from schemas.client_schema import ClientCreate, ClientUpdate, ClientResponse
from services import client_service
from db.session import get_db
from contextlib import contextmanager

client_bp = Blueprint("clients", __name__, url_prefix="/clients")

@client_bp.route("/", methods=["POST"])
def create():
    with db_session() as db:
        data = ClientCreate(**request.json)
        client = client_service.create_client(db, data)
        
        return jsonify(ClientResponse.model_validate(client).model_dump()), 201

@client_bp.route("/", methods=["GET"])
def get_all():
    with db_session() as db:
        clients = client_service.get_clients(db)
        return jsonify([ClientResponse.model_validate(c).model_dump() for c in clients]), 200

@client_bp.route("/<int:client_id>", methods=["GET"])
def get(client_id):
    with db_session() as db:
        client = client_service.get_client(db, client_id)
        if client:
            return ClientResponse.model_validate(client).model_dump_json(), 200
        abort(404, "Client not found")

@client_bp.route("/<int:client_id>", methods=["PUT"])
def update(client_id):
    with db_session() as db:
        data = ClientUpdate(**request.json)
        updated = client_service.update_client(db, client_id, data)
        if not updated:
            abort(404, "Client not found")
        return jsonify({"Status": "Client updated"}), 200

@client_bp.route("/<int:client_id>", methods=["DELETE"])
def delete(client_id):
    with db_session() as db:
        client = client_service.get_client(db, client_id)
        if not client:
            abort(404, "Client not found")
        if client_service.delete_client(db, client):
            return "", 204
        abort(501, "Error deleting client")

@contextmanager
def db_session():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()
