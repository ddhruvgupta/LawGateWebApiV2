from datetime import datetime
from clients.databaseClient import DatabaseClient

class Client:
    def __init__(self, client_id=None, client_name=None, client_email=None, client_phone=None, blob_storage_container_name=None, created_at=None):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_phone = client_phone
        self.blob_storage_container_name = blob_storage_container_name
        self.created_at = created_at or datetime.utcnow()
    
    def populate(self, obj):
        if obj.get('client_id'):
            self.client_id = obj['client_id']
        if obj.get('client_name'):
            self.client_name = obj['client_name']
        if obj.get('client_email'):
            self.client_email = obj['client_email']
        if obj.get('client_phone'):
            self.client_phone = obj['client_phone']
        if obj.get('blob_storage_container_name'):
            self.blob_storage_container_name = obj['blob_storage_container_name']
        if obj.get('created_at'):
            self.created_at = obj['created_at']

    def __repr__(self):
        return f"Client(client_id={self.client_id}, client_name={self.client_name}, client_email={self.client_email}, client_phone={self.client_phone}, blob_storage_container_name={self.blob_storage_container_name}, created_at={self.created_at})"
    
    def __str__(self):
        return f"Client(client_id={self.client_id}, client_name={self.client_name}, client_email={self.client_email}, client_phone={self.client_phone}, blob_storage_container_name={self.blob_storage_container_name}, created_at={self.created_at})"

    def to_dict(self):
        return {
            'client_id': self.client_id,
            'client_name': self.client_name,
            'client_email': self.client_email,
            'client_phone': self.client_phone,
            'blob_storage_container_name': self.blob_storage_container_name,
            'created_at': self.created_at
        }

