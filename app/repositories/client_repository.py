from app.models.client_model import Client
from app.db.session import get_db

class ClientRepository:
    def __init__(self):
        self.db = next(get_db())

    def create(self, data: dict):
        client = Client(**data)
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def get_all(self):
        return self.db.query(Client).all()

    def get_by_id(self, client_id: int):
        return self.db.query(Client).filter(Client.id == client_id).first()

    def update(self, client, data: dict):
        for key, value in data.items():
            setattr(client, key, value)
        self.db.commit()
        self.db.refresh(client)
        return client

    def delete(self, client):
        self.db.delete(client)
        self.db.commit()