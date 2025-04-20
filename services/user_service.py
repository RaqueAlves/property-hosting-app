from repository.user_repository import UserRepository
from model.user import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.repository = user_repository

    def create_user(self, name, email, user_type):
        if self.get_user_by_email(email):
            raise ValueError("Usuário com esse e-mail já existe.")
        
        new_user = User(name, email, user_type)
        self.repository.add_user(new_user)

    def get_user_by_email(self, email):
        users = self.repository.list_users()
        for user in users:
            if user.email == email:
                return user
        return None

    def get_user_by_id(self, user_id):
        users = self.repository.list_users()
        for user in users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id, name=None, email=None, user_type=None):
        user = self.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")
        
        if name:
            user.name = name
        if email:
            user.email = email
        if user_type:
            user.user_type = user_type

        self.repository.save_users()  # Atualiza o repositório

    def list_users(self):
        return self.repository.list_users()
