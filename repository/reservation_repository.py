import json
from model.reservation import Reservation

class ReservationRepository:
    FILE_PATH = "reservations.json"

    def __init__(self):
        self.__reservations = self.load_reservations()

    def add_reservation(self, reservation: Reservation):
        self.__reservations.append(reservation)
        self.save_reservations()

    def list_reservations(self):
        return [r.to_dict() for r in self.__reservations]
    
    def list_obj_reservations(self):
        return [r for r in self.__reservations]

    def load_reservations(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Reservation.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_reservations(self):
        data = [r.to_dict() for r in self.__reservations]
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def remove_reservation_by_id(self, reservation_id: str):
        original_count = len(self.__reservations)
        self.__reservations = [r for r in self.__reservations if r.id != reservation_id]

        if len(self.__reservations) < original_count:
            self.save_reservations()
            return True
        return False
