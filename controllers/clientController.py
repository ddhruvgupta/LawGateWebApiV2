import uuid
from clients.DatabaseClient import DatabaseClient
from clients.AzureBlobStorageClient import AzureBlobStorageClient
from models.clientModel import Client
from helpers.ClientDataValidator import ClientDataValidator


class ClientController:
    def __init__(self):
        self.database = DatabaseWrapper()
        self.blob_client = AzureBlobStorageClient()
        self.validator = ClientDataValidator()

    def create_client(self, request):
        blob_container_name = str(uuid.uuid4())

        isContainerCreated = self.blob_client.create_container(blob_container_name)
        if isContainerCreated:
            client = Client()
            client.populate(request)
            client.blob_storage_container_name = blob_container_name
            try:
                data = self.database.create_client(client)
            except Exception as e:
                self.blob_client.delete_container(blob_container_name)
                return None
        return data

    def get_client(self, client_id):
        return self.database.read_client(client_id)
        
    def get_all_clients(self):
        return self.database.fetch_all_clients()

    def update_client(self, client_id, data):
        self.validator.validate_client_data(data)
        if self.get_client(client_id):
            return self.database.update_client(client_id, data)
        return False
    
    def delete_client(self, client_id):
        '''removed the database entry and the related blob storage container'''
        if self.get_client(client_id):
            try:
                self.blob_client.delete_container(client_id)
                return self.database.delete_client(client_id)
            except Exception as e:
                return e
        return False


class DatabaseWrapper:
    def __init__(self):
        self.db_client = DatabaseClient()

    def create_client(self, client: Client):
        query = """
        INSERT INTO Clients (client_name, client_email, client_phone, blob_storage_container_name)
        VALUES (%s, %s, %s, %s)
        """
        print("params recieved:",client)
        params = (client.client_name, client.client_email, client.client_phone, client.blob_storage_container_name)
        try:
            client_id = self.db_client.insert(query, params)
            return client_id
        except Exception as e:
            print(f"Error: {e}")
            return e

    def read_client(self, client_id):
        query = "SELECT * FROM Clients WHERE client_id = %s"
        params = (client_id,)
        try:
            return self.db_client.fetch_filtered(query, params)
        except Exception as e:
            print(f"Error: {e}")
            return e

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
        try:
            rows_updated = self.db_client.update(query, tuple(params))
            if rows_updated == 1:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return e

    def delete_client(self, client_id):
        query = "DELETE FROM Clients WHERE client_id = %s"
        params = (client_id,)
        try:
            self.db_client.delete(query, params)
        except Exception as e:
            print(f"Error: {e}")
            return e

    def find_client_by_name(self, client_name):
        query = "SELECT * FROM Clients WHERE client_name = %s"
        params = (client_name,)
        try:
            return self.db_client.fetch_filtered(query, params)
        except Exception as e:
            print(f"Error: {e}")
            return e

    def fetch_all_clients(self):
        query = "SELECT * FROM Clients"
        try:
            return self.db_client.fetch_all(query)
        except Exception as e:
            print(f"Error: {e}")
            return e

# Example usage
# if __name__ == "__main__": 
#     db_client = DatabaseClient(database='lawgateV2', user='root', password='Test123!')
#     client_model = ClientModel(db_client)
    
#     # Create a new client
#     new_client = Client(client_name='John Doe', client_email='john.doe@example.com', client_phone='1234567890', blob_storage_container_name='container_name')
#     client_model.create_client(new_client)

#     # Read a client
#     client = client_model.read_client(1)
#     print("Client:", client)

#     # Update a client
#     updated_client = Client(client_id=1, client_name='Jane Doe')
#     client_model.update_client(updated_client)

#     # Delete a client
#     client_model.delete_client(1)