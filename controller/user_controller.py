from controller.property_controller import PropertyController
from controller.reservation_controller import ReservationController
from view.user_view import UserView

class UserController:

    def __init__(self):
        self.__property_controller = PropertyController()
        self.__reservation_controller = ReservationController()
        self.__view = UserView()

    def start_system(self):
        self.initial_system_page()

    def end_system(self):
        exit(0)

    def new_user(self):
        pass

    def login(self):
        data_login = self.__view.get_data_user()

        name_user = data_login[0]
        email_user = data_login[1]

    def initial_system_page(self):
        options = {
            1: self.login,
            2: self.new_user,
            3: self.end_system
        }
        
        while True:
            choose = self.__view.system_menu()
            if choose in options:
                options[choose]()
            else:
                self.__view.show_message(msg="Escolha um numero entre as opções.")