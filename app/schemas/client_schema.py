from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ClientCreate(BaseModel):
    client_name: str
    client_email: Optional[EmailStr]
    client_phone: Optional[str]
    blob_storage_container_name: Optional[str]

class ClientUpdate(BaseModel):
    client_id: int
    client_name: Optional[str]
    client_email: Optional[EmailStr]
    client_phone: Optional[str]
    blob_storage_container_name: Optional[str]

class ClientResponse(ClientCreate):
    client_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
