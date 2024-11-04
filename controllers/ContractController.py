from clients.AzureBlobStorageClient import AzureBlobStorageClient
from clients.DatabaseClient import DatabaseClient
from controllers.ClientController import ClientController
from models.contractModel import Contract
import uuid

class ContractController: 
    def __init__(self):
        self.blob_client = AzureBlobStorageClient()
        self.db_client = DatabaseClient()
        self.contract = Contract()
        self.client_controller = ClientController()

    def create_contract(self, contract_data, file):
        query = """
        INSERT INTO contracts (contract_name, client_id)
        VALUES (%s, %s, %s)
        """
        
        params = (contract_data.contract_name, contract_data.client_id)
        return self.db_client.insert(query, params)

    def get_contract_by_id(self, contract_id):
        query = "SELECT * FROM contracts WHERE contract_id = %s"
        params = (contract_id,)
        return self.db_client.fetch_filtered(query, params)

    def get_all_contracts(self):
        query = "SELECT * FROM contracts"
        return self.db_client.fetch_all(query)

    def update_contract(self, contract_id, contract_name=None, client_id=None, contract_document_link=None):
        updates = []
        params = []

        if contract_name:
            updates.append("contract_name = %s")
            params.append(contract_name)
        if client_id:
            updates.append("client_id = %s")
            params.append(client_id)
        if contract_document_link:
            updates.append("document_link = %s")
            params.append(contract_document_link)

        params.append(contract_id)
        query = f"UPDATE contracts SET {', '.join(updates)} WHERE contract_id = %s"
        return self.db_client.insert(query, params)

    def delete_contract(self, contract_id):
        query = "DELETE FROM contracts WHERE contract_id = %s"
        params = (contract_id,)
        return self.db_client.insert(query, params)
    
    def upload_contract_file(self, container_name, file):
        blob_name = "contracts/"+ str(uuid.uuid4())

        return self.blob_client.upload_file(file,blob_name, container_name)


