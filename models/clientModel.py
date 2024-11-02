from datetime import datetime

class Client:
    def __init__(self, client_id=None, client_name=None, client_email=None, client_phone=None, blob_storage_container_name=None, created_at=None):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_phone = client_phone
        self.blob_storage_container_name = blob_storage_container_name
        self.created_at = created_at or datetime.utcnow()

class ClientModel:
    def __init__(self, db_client: DatabaseClient):
        self.db_client = db_client

    def create_client(self, client: Client):
        query = """
        INSERT INTO Clients (client_name, client_email, client_phone, blob_storage_container_name)
        VALUES (%s, %s, %s, %s)
        """
        params = (client.client_name, client.client_email, client.client_phone, client.blob_storage_container_name)
        self.db_client.fetch_filtered(query, params)

    def read_client(self, client_id):
        query = "SELECT * FROM Clients WHERE client_id = %s"
        params = (client_id,)
        return self.db_client.fetch_filtered(query, params)

    def update_client(self, client: Client):
        query = "UPDATE Clients SET "
        params = []
        if client.client_name:
            query += "client_name = %s, "
            params.append(client.client_name)
        if client.client_email:
            query += "client_email = %s, "
            params.append(client.client_email)
        if client.client_phone:
            query += "client_phone = %s, "
            params.append(client.client_phone)
        if client.blob_storage_container_name:
            query += "blob_storage_container_name = %s, "
            params.append(client.blob_storage_container_name)
        query = query.rstrip(', ')  # Remove trailing comma
        query += " WHERE client_id = %s"
        params.append(client.client_id)
        self.db_client.fetch_filtered(query, tuple(params))

    def delete_client(self, client_id):
        query = "DELETE FROM Clients WHERE client_id = %s"
        params = (client_id,)
        self.db_client.fetch_filtered(query, params)

# Example usage
if __name__ == "__main__": 
    db_client = DatabaseClient(database='lawgateV2', user='root', password='Test123!')
    client_model = ClientModel(db_client)
    
    # Create a new client
    new_client = Client(client_name='John Doe', client_email='john.doe@example.com', client_phone='1234567890', blob_storage_container_name='container_name')
    client_model.create_client(new_client)

    # Read a client
    client = client_model.read_client(1)
    print("Client:", client)

    # Update a client
    updated_client = Client(client_id=1, client_name='Jane Doe')
    client_model.update_client(updated_client)

    # Delete a client
    client_model.delete_client(1)