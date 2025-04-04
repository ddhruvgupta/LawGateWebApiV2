from sqlalchemy.orm import Session
from models.contract_model import Contract

class ContractRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_contract(self, contract: Contract):
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def get_contract_by_id(self, contract_id: int):
        return self.db.query(Contract).filter(Contract.contract_id == contract_id).first()

    def get_all_contracts(self):
        return self.db.query(Contract).all()

    def update_contract(self, contract_id: int, updates: dict):
        contract = self.db.query(Contract).filter(Contract.contract_id == contract_id).first()
        if not contract:
            return None
        for key, value in updates.items():
            setattr(contract, key, value)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def delete_contract(self, contract_id: int):
        contract = self.db.query(Contract).filter(Contract.contract_id == contract_id).first()
        if contract:
            self.db.delete(contract)
            self.db.commit()
        return contract
