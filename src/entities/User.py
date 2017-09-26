class User_Get_Response(object):
    def __init__(self, email, phone_number, full_name, key, account_key, metadata):
        self.email = email
        self.phone_number = phone_number
        self.full_name = full_name
        self.key = key
        self.account_key = account_key
        self.metadata = metadata

class Password(object):
    def __init__(self, hashed_password, password_salt):
        self.hashed_password = hashed_password
        self.password_salt = password_salt


class User_Post_Request(object):
    def __init__(self, email, phone_number, full_name, password, metadata, key=None, account_key=None, id=None):
        self.id = id
        self.email = email
        self.phone_number = phone_number
        self.full_name = full_name
        self.password = password
        self.key = key
        self.account_key = account_key
        self.metadata = metadata