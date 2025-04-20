import uuid
from datetime import date

from model.property import Property

class Reservation:
    VALID_STATUSES = {"pendente", "confirmada", "cancelada"}

    def __init__(self,
                 property_id: str,
                 client_id: str,
                 start_date: date,
                 end_date: date,
                 status: str,
                 id: str = None):
        
        self.id = id or str(uuid.uuid4())
        self.status = status
        self.property_id = property_id
        self.client_id = client_id
        self.start_date = start_date
        self.end_date = end_date

    @property
    def property_id(self):
        return self.__property_id
    
    @property_id.setter
    def property_id(self, property_id):
        self.__property_id = property_id
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Status inválido: '{status}'. Os status permitidos são: {', '.join(self.VALID_STATUSES)}.")
        self.__status = status
    
    @property
    def client_id(self):
        return self.__client_id
    
    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id

    @property
    def start_date(self):
        return self.__start_date
    
    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "property_id": self.property_id,
            "client_id": self.client_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat()
        }
    
    @staticmethod
    def from_dict(data):
        return Reservation(
            id=data["id"],
            status=data["status"],
            property_id=data["property_id"],
            client_id=data["client_id"],
            start_date=date.fromisoformat(data["start_date"]),
            end_date=date.fromisoformat(data["end_date"])
        )
