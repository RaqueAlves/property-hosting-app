import json
from model.property import Property

class PropertyRepository:
    FILE_PATH = "property.json"

    def __init__(self):
        self.__property = self.load_properties()
    
    '''Recebe um usuário, 
    adiciona-o à lista de usuários
    e chama a função save_users'''
    def add_property(self, property):
        if not isinstance(property, Property):
            raise TypeError("'property' deve ser um objeto da classe 'Property'.")
        self.__property.append(property)
        self.save_properties(self.__property)

    '''tenta ler o arquivo json,
    converte os dados para um objeto
    da classe User e retorna 
    uma lista de objetos'''
    def load_properties(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                properties_data = json.load(file)

                properties_object = []
                for pro in properties_data:
                    property = Property(**pro)
                    properties_object.append(property)

                return properties_object
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do aruivo'''
    def save_properties(self, properties):
        properties_data = []
        for pro in properties:
            properties_data.append(pro.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(properties_data, file, ensure_ascii=False, indent=4)
        
        self.__property = properties

    '''retorna a lista 'users' 
    de objetos 'Usuario' 
    convertida em dicionário'''
    def list_properties(self):
        return [property.to_dict() for property in self.__property]
    
    '''retorna a lista 'users' 
    de objetos 'Usuario' '''
    def list_objects_properties(self):
        return [property for property in self.__property]
    
    def get_by_id(self, id):
        list = self.list_objects_properties()

        for li in list:
            if li.id == id:
                return li