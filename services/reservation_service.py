from repository.reservation_repository import ReservationRepository
from repository.property_repository import PropertyRepository
from model.reservation import Reservation

class ReservationService:
    def __init__(self, 
                 reservation_repository: ReservationRepository,
                 property_repository: PropertyRepository):
        self.repository = reservation_repository
        self.property_repository = property_repository

    def create_reservation(self, property_id, client_id, start_date, end_date):
        property = self.property_repository.get_by_id(property_id)
        if not property:
            raise ValueError("Imóvel não encontrado.")
        
        if not self.is_property_available(property_id, start_date, end_date):
            raise ValueError("Reserva falhou. Dados conflitantes.")

        new_reservation = Reservation(property_id, client_id, start_date, end_date, "pendente", None)
        self.repository.add_reservation(new_reservation)

        return new_reservation

    def confirm_reservation(self, reservation_id):
        re = self.get_by_id(reservation_id)
        if re:
            re.status = "confirmada"
            self.repository.save_reservations()

    def cancel_reservation(self, reservation_id):
        removed = self.repository.remove_reservation_by_id(reservation_id)
        if not removed:
            raise ValueError("Reserva não encontrada para remoção.")

    def is_property_available(self, property_id, start_date, end_date):
        reservations = self.list_reservation_by_property(property_id)

        for re in reservations:
            if not re.status != "confirmada":
                continue
            
            if not (end_date < re.start_date or start_date > re.end_date):
                return False
            
        return True

    def list_reservation_by_property(self, property_id):
        reservation_in_this_property = []
        list_obj_reservations = self.repository.list_obj_reservations()

        for reservation in list_obj_reservations:
            if reservation.property_id == property_id:
                reservation_in_this_property.append(reservation)

        return reservation_in_this_property
    
    def get_by_id(self, id):
        reservations = self.repository.list_obj_reservations()
        for re in reservations:
            if re.id == id:
                return re
        return False