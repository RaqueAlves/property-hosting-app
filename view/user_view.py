

class UserView:

    def system_menu(self):
        print("entrou no view")
        print("==== SISTEMA DE LOCAÇÃO DE IMÓVEIS ====")

        choose = int(input("1. Login\n"+
                       "2. Cadastro\n"+
                       "3. Sair\n"))
        return choose
    
    def show_message(self, msg):
        print(msg)
    
    def create_data_user(self):
        print("============== CADASTRO ===============")
        name = str(input("Nome: \n"))
        email = str(input("Email: \n"))
        type = str(input("Tipo de Conta: \n" +
                         "Locatário(1)\n" +
                         "Locador(2)\n"))

        return [name, email, type]

    def get_data_user(self):
        print("================ LOGIN ================")
        name = str(input("Nome: \n"))
        email = str(input("Email: \n"))
        type = str(input("Tipo de Conta: \n"))

        return [name, email]

    def lista_usuario(self):
        pass

    def modifica_usuario(self):
        pass

    