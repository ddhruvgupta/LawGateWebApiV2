class Contract:
    def __init__(self, contract_id=None, contract_name=None, client_id=None, contract_document_link=None):
        self.contract_id = contract_id
        self.contract_name = contract_name
        self.client_id = client_id
        self.contract_document_link = contract_document_link

    def populate(self, obj):
        if obj.get('contract_id'):
            self.contract_id = obj['contract_id']
        if obj.get('contract_name'):
            self.contract_name = obj['contract_name']
        if obj.get('client_id'):
            self.client_id = obj['client_id']
        if obj.get('contract_document_link'):
            self.contract_document_link = obj['contract_document_link']
