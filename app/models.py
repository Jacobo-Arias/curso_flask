from flask_login import UserMixin #este UserMixing ya implementa las propiedades que requiere flask-login
from .mongo_services import get_user

class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        ;param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password
    
    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username = user_doc['user'], password = user_doc['password']
        )

        return UserModel(user_data)
