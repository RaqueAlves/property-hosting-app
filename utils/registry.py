'''o dicionario guarda 
as classes registradas'''
USER_CLASSES = {}

'''essa função é um decorator'''
def register_user_class(cls):
    USER_CLASSES[cls.__name__] = cls
    return cls
