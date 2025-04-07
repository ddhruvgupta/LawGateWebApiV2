from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Contract(Base):
    __tablename__ = "contracts"

    contract_id = Column(Integer, primary_key=True, autoincrement=True)
    contract_name = Column(String(255), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)
    document_link = Column(String(512), nullable=True)

    client = relationship("Client", back_populates="contracts")