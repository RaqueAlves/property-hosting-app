from model.user import User
from utils.registry import register_user_class

@register_user_class
class UserClient(User):
    def __init__(self, name, email, id = None):
        super().__init__(name, email, id)