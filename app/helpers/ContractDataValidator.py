class ContractDataValidator:
    required_fields = ['contract_name', 'client_id', 'contract_document_link']

    

    @staticmethod
    def validate_contract_id(contract_id):
        if contract_id and isinstance(contract_id, int):
            return True, None
        return False, "Invalid contract ID"

    @staticmethod
    def validate_contract_name(contract_name):
        if contract_name and isinstance(contract_name, str) and len(contract_name) > 0:
            return True, None
        return False, "Invalid contract name"

    @staticmethod
    def validate_client_id(client_id):
        if client_id and isinstance(client_id, int):
            return True, None
        return False, "Invalid client ID"

    @staticmethod
    def validate_contract_document_link(contract_document_link):
        if contract_document_link and isinstance(contract_document_link, str) and len(contract_document_link) > 0:
            return True, None
        return False, "Invalid contract document link"