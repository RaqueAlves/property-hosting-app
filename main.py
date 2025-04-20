import uuid
from model.user_owner import UserOwner
from model.user_client import UserClient
from model.property import Property
from repository.user_repository import UserRepository
from repository.property_repository import PropertyRepository
from datetime import date
from model.reservation import Reservation
from repository.reservation_repository import ReservationRepository

# Criação dos objetos
owner = UserOwner(name="Ana Locadora", email="ana@exemplo.com", id=str(uuid.uuid4()))
client = UserClient(name="Carlos Inquilino", email="carlos@exemplo.com", id=str(uuid.uuid4()))

# Salvando com o UserRepository
repository = UserRepository()
repository.add_user(owner)
repository.add_user(client)


# Criando um exemplo de propriedade
property = Property(
    title="Apartamento na Praia",
    description="Apartamento com vista para o mar, 2 quartos e ar-condicionado.",
    address="Rua das Ondas, 123 - Florianópolis, SC",
    daily_rate=350.0,
    availability=[
        {"start": "2025-05-01", "end": "2025-05-10"},
        {"start": "2025-06-01", "end": "2025-06-15"}
    ],
    owner_id=str(uuid.uuid4()))
                    

# Salvando com o PropertyRepository
repository = PropertyRepository()
repository.add_property(property)

# Criar a reserva
reservation = Reservation(
    property_id="abc123",
    client_id="client456",
    start_date=date(2025, 6, 1),
    end_date=date(2025, 6, 5),
    status="pendente"
)

# Salvar no repositório
repo = ReservationRepository()
repo.add_reservation(reservation)

# Mostrar resultado
for r in repo.list_reservations():
    print(r)

