from azure.storage.blob import BlobServiceClient
import io, os
from flask import send_file
from dotenv import load_dotenv
import logging

load_dotenv()

class AzureBlobStorageClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AzureBlobStorageClient, cls).__new__(cls)
        return cls._instance

    def __init__(self, connection_string=None):
        if not hasattr(self, 'initialized'):
            if connection_string is None:
                connection_string = os.getenv("BLOB_CONNECTION_STRING")
            if not connection_string:
                raise ValueError("BLOB_CONNECTION_STRING environment variable is not set")
            try:
                self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            except Exception as e:
                logging.error("Failed to create BlobServiceClient: %s", e)
                raise
            self.initialized = True

    # def upload_file(self, file_path, blob_name, container_name):
    #     try:
    #         blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    #         with open(file_path, "rb") as data:
    #             blob_client.upload_blob(data)
    #         logging.info(f"File {file_path} uploaded to blob {blob_name}.")
    #     except Exception as e:
    #         logging.error("Failed to upload file: %s", e)
    #         raise

    def upload_file(self, file, blob_name, container_name):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(file)
            logging.info(f"File uploaded to blob {blob_name}.")
        except Exception as e:
            logging.error("Failed to upload file from browser: %s", e)
            raise


    def download_file(self, blob_name, custom_name=None):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=blob_name)
            stream = io.BytesIO()
            stream.write(blob_client.download_blob().readall())
            stream.seek(0)
            download_name = custom_name if custom_name else blob_name
            return send_file(stream, as_attachment=True, download_name=download_name)
        except Exception as e:
            logging.error("Failed to download file: %s", e)
            raise

    def delete_file(self, container_name, blob_name):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.delete_blob()
            logging.info(f"Blob {blob_name} deleted from container {container_name}.")
        except Exception as e:
            logging.error("Failed to delete file: %s", e)
            raise

    def create_container(self, container_name):
        try:
            self.blob_service_client.create_container(container_name)
            logging.info(f"Container {container_name} created successfully.")
            return True
        except Exception as e:
            logging.error("Failed to create container: %s", e)
            return False

# Example usage:
# Note: The connection string can be found in the Azure portal under the "Access keys" section of the storage account.

# connection_string = "DefaultEndpointsProtocol=https;AccountName=csg10032000b0467fa5;AccountKey=M1S5aSIHJlPjf+bpmEbSvt/7U2J70r3bzz0xFElrYmm0P8UqU94CzT6DCp+ppDSuWbg4kf0058Kn+AStabE/fw==;EndpointSuffix=core.windows.net"
# container_name = "test"
# client = AzureBlobStorageClient(connection_string)
# testFilePath = r'C:\Users\Dhruv-PC\Documents\Tracking.txt'

# # Generate a GUID for the blob file name
# blob_name = str(uuid.uuid4()) + ".txt"
# client.upload_file(testFilePath, blob_name, container_name)
# blob_name = "dc0ef768-386e-42a5-9298-ad1f1e508823.txt"
# client.download_file(blob_name, r'C:\Users\Dhruv-PC\Documents\Tracking1.txt')
