import re
import uuid

class User:
    def __init__(self, 
                 name: str, 
                 email: str,
                 id: str = None):
        
        self.name = name
        self.email = email
        self.id = id or str(uuid.uuid4())

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("'name' deve ser uma string.")    
        if not len(name) >= 3:
            raise ValueError("'name' deve ter no mínimo 3 caracteres.")
        self.__name = name
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("'email' deve ser uma string.")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", email):
                raise ValueError("Formato de email inválido.")
        self.__email = email

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    def to_dict(self):
        return {
            "nome": self.name,
            "email": self.email,
            "id": self.id,
            "type": self.__class__.__name__
        }