from pydantic import BaseModel
from typing import Optional

class ContractCreate(BaseModel):
    contract_name: str
    client_id: int

class ContractUpdate(BaseModel):
    contract_name: Optional[str] = None
    client_id: Optional[int] = None
    document_link: Optional[str] = None

class ContractResponse(ContractCreate):
    contract_id: int
    document_link: Optional[str]
