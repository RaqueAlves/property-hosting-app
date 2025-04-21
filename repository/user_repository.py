import json
from utils.registry import USER_CLASSES
from model.user import User

class UserRepository:
    FILE_PATH = "user.json"

    def __init__(self):
        self.__users = self.load_users()
    
    '''Recebe um usuário, 
    adiciona-o à lista de usuários
    e chama a função save_users'''
    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("'user' deve ser um objeto da classe 'Usuario'.")
        self.__users.append(user)
        self.save_users(self.__users)

    '''tenta ler o arquivo json. 
    Identifica o tipo de usuário 
    e em seguida o remove. Converte 
    os dados do dicionário para um
    objeto. Adiciona os objetos 
    a lista de objetos.
    Retorna a lista de objetos.'''
    def load_users(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                users_data = json.load(file)
                users_object = []

                for user_data in users_data:
                    user_type = user_data.pop("type", "User")
                    cls = USER_CLASSES.get(user_type, User)
                    user = cls(**user_data)
                    users_object.append(user)

                return users_object
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def update_user(self, updated_user):
        for i, user in enumerate(self.__users):
            if user.id == updated_user.id:
                self.__users[i] = updated_user
                self.save_users(self.__users)
                return
            raise ValueError("Usuário não encontrado para atualização.")

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do arquivo'''
    def save_users(self, users):
        users_data = []
        for user in users:
            users_data.append(user.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(users_data, file, ensure_ascii=False, indent=4)
        
        self.__users = users

    '''retorna a lista 'users' 
    de objetos 'Usuario' 
    convertida em dicionário'''
    def list_users(self):
        return [user.to_dict() for user in self.__users]
    
    '''retorna a lista 'users'
    de objetos 'Usuario' '''
    def list_objects_users(self):
        return [user for user in self.__users]