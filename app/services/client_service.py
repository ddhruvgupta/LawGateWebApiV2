from repositories import client_repository
from sqlalchemy.orm import Session
from schemas.client_schema import ClientCreate, ClientUpdate
from models.client_model import Client

def create_client(db: Session, data: ClientCreate) -> Client:
    return client_repository.create_client(db, data.model_dump())

def get_clients(db: Session) -> list[Client]:
    return client_repository.get_all_clients(db)

def get_client(db: Session, client_id: int) -> Client | None:
    return client_repository.get_client_by_id(db, client_id)

def update_client(db: Session, client_id: int, data: ClientUpdate) -> Client | None:
    client = get_client(db, client_id)
    if not client:
        return None
    return client_repository.update_client(db, client, data.dict(exclude_unset=True))

def delete_client(db: Session, client_id: int) -> bool:
    client = get_client(db, client_id)
    if not client:
        return False
    client_repository.delete_client(db, client)
    return True


