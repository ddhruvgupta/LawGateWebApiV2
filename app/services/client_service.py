from app.repositories.client_repository import ClientRepository
from app.schemas.client_schema import ClientCreate, ClientUpdate

class ClientService:
    def __init__(self):
        self.client_repository = ClientRepository()

    def create_client(self, data: ClientCreate):
        return self.client_repository.create(data.dict())

    def get_all_clients(self):
        return self.client_repository.get_all()

    def get_client(self, client_id: int):
        return self.client_repository.get_by_id(client_id)

    def update_client(self, client_id: int, data: ClientUpdate):
        client = self.client_repository.get_by_id(client_id)
        if not client:
            return None
        return self.client_repository.update(client, data.dict(exclude_unset=True))

    def delete_client(self, client_id: int):
        client = self.client_repository.get_by_id(client_id)
        if not client:
            return False
        self.client_repository.delete(client)
        return True


