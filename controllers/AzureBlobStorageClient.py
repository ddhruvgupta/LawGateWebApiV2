from azure.storage.blob import BlobServiceClient
import uuid, io
from flask import send_file

class AzureBlobStorageClient:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def upload_file(self, file_path, container_name, blob_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File {file_path} uploaded to blob {blob_name}.")

    def download_file(self, container_name, blob_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        stream = io.BytesIO()
        stream.write(blob_client.download_blob().readall())
        stream.seek(0)
        return send_file(stream, as_attachment=True, download_name=blob_name)

    def create_container(self, new_container_name):
        try:
            new_container_client = self.blob_service_client.create_container(new_container_name)
            print(f"Container {new_container_name} created successfully.")
        except Exception as e:
            print(f"Failed to create container {new_container_name}: {e}")


# Example usage:
# Note: The connection string can be found in the Azure portal under the "Access keys" section of the storage account.

connection_string = "DefaultEndpointsProtocol=https;AccountName=csg10032000b0467fa5;AccountKey=M1S5aSIHJlPjf+bpmEbSvt/7U2J70r3bzz0xFElrYmm0P8UqU94CzT6DCp+ppDSuWbg4kf0058Kn+AStabE/fw==;EndpointSuffix=core.windows.net"
container_name = "lawgate-file-storage"
client = AzureBlobStorageClient(connection_string, container_name)
testFilePath = r'C:\Users\Dhruv-PC\Documents\Tracking.txt'

# Generate a GUID for the blob file name
blob_name = str(uuid.uuid4()) + ".txt"
client.upload_file(testFilePath, blob_name)
client.download_file(blob_name, r"C:\Users\Dhruv-PC\Downloads\Tracking.txt")

