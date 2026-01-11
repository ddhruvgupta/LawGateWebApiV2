from flask_smorest import Blueprint
from flask import abort, jsonify
from app.schemas.client_schema import ClientCreate, ClientUpdate, ClientResponse
from app.services.client_service import ClientService

class ClientController:
    def __init__(self, client_service: ClientService):
        self.client_service = client_service
        self.blueprint = Blueprint("clients", "clients", url_prefix="/clients", description="Operations on clients")
        self._register_routes()

    def _register_routes(self):
        # Dynamically apply decorators
        self.blueprint.route("/", methods=["POST"])(
            self.blueprint.arguments(ClientCreate)(self.create)
        )
        self.blueprint.route("/", methods=["GET"])(self.get_all)
        self.blueprint.route("/<int:client_id>", methods=["GET"])(self.get)
        self.blueprint.route("/<int:client_id>", methods=["PUT"])(
            self.blueprint.arguments(ClientUpdate)(self.update)
        )
        self.blueprint.route("/<int:client_id>", methods=["DELETE"])(self.delete)

    def create(self, data):
        """
        Create a new client.
        """
        client = self.client_service.create_client(data)
        return jsonify(ClientResponse.model_validate(client).model_dump()), 201

    def get_all(self):
        """
        Retrieve all clients.
        """
        clients = self.client_service.get_all_clients()
        return jsonify([ClientResponse.model_validate(c).model_dump() for c in clients]), 200

    def get(self, client_id):
        """
        Retrieve a client by their ID.
        """
        client = self.client_service.get_client(client_id)
        if client:
            return ClientResponse.model_validate(client).model_dump_json(), 200
        abort(404, "Client not found")

    def update(self, data, client_id):
        """
        Update a client's information by their ID.
        """
        updated = self.client_service.update_client(client_id, data)
        if not updated:
            abort(404, "Client not found")
        return jsonify({"Status": "Client updated"}), 200

    def delete(self, client_id):
        """
        Delete a client by their ID.
        """
        deleted = self.client_service.delete_client(client_id)
        if deleted:
            return "", 204
        abort(404, "Client not found")

    @staticmethod
    def create_controller():
        """
        Factory method to create and configure the ClientController.
        """
        client_service = ClientService()  # Instantiate the service
        return ClientController(client_service)


# Create a singleton instance and export the blueprint
_controller = ClientController.create_controller()
client_bp = _controller.blueprint
