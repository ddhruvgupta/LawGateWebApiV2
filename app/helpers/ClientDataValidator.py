import re

class ClientDataValidator:
    required_fields = ['client_name', 'client_email', 'client_phone']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_regex = r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$'

    @staticmethod
    def validate_all(data):
        '''validate all required fields in client are formatted correctly'''
        is_valid, message = ClientDataValidator.validate_all_required_fields(data)
        if not is_valid:
            return False, message

        is_valid, message = ClientDataValidator.validate_email(data['client_email'])
        if not is_valid:
            return False, message
        
        is_valid, message = ClientDataValidator.validate_phone(data['client_phone'])
        if not is_valid:
            return False, message

        return True, None

    @staticmethod
    def validate_all_required_fields(data):
        for field in ClientDataValidator.required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
        return True, None

    @staticmethod
    def validate_email(email):
        if re.match(ClientDataValidator.email_regex, email):
            return True, None
        return False, "Invalid email format"

    @staticmethod
    def validate_phone(phone):
        if re.match(ClientDataValidator.phone_regex, phone):
            return True, None
        return False, "Invalid phone number format"