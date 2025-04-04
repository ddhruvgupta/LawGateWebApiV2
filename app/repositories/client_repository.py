from models.client_model import Client
from sqlalchemy.orm import Session

def create_client(db: Session, client_data: dict) -> Client:
    client = Client(**client_data)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def get_all_clients(db: Session) -> list[Client]:
    return db.query(Client).all()

def get_client_by_id(db: Session, client_id: int) -> Client | None:
    return db.query(Client).filter(Client.client_id == client_id).first()

def update_client(db: Session, client: Client, update_data: dict) -> Client:
    for key, value in update_data.items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

def delete_client(db: Session, client: Client):
    db.delete(client)
    db.commit()
