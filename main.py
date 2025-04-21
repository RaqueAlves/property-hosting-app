import uuid
from model.user_owner import UserOwner
from model.user_client import UserClient
from model.property import Property
from repository.user_repository import UserRepository
from repository.property_repository import PropertyRepository
from datetime import date
from model.reservation import Reservation
from repository.reservation_repository import ReservationRepository
from services.user_service import UserService

if "__main__" == __name__:
    #criando dois usuários
    repositorio = UserRepository()
    user1 = UserService(repositorio)
    
    # user1.create_user(
    # name="Raquel Alves Pinto",
    # email="raquelavsp7@gmail.com",
    # user_type="Locador"
    # )

    # user1.create_user(
    #     name="Susana Banana",
    #     email="sus_peita@gmail.com",
    #     user_type="Cliente"
    # )

    #atualiando um dos usuários
    usuario = user1.get_user_by_email(email="sus_peita@gmail.com")
    user1.update_user(user_id= usuario.id, name="Susana Alves Pinto")