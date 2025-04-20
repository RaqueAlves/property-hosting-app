import uuid
from datetime import datetime

class Property:

    def __init__(self,
                 title: str,
                 description: str,
                 address: str,
                 daily_rate: float,
                 availability: list = None,
                 owner_id: str = None,
                 id: str = None):
        
        self.title = title
        self.description = description
        self.address = address
        self.daily_rate = daily_rate
        #representa o período em que o imóvel pode ser reservado
        self.availability = availability or []
        self.owner_id = owner_id or None
        self.id = id or str(uuid.uuid4())

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("'title' deve ser uma string.")    
        if not len(title) >= 8:
            raise ValueError("'title' deve ter no mínimo 8 caracteres.")
        self.__title = title
        
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("'description' deve ser uma string.")    
        if len(description) < 300 and len(description) > 1500:
            raise ValueError("'description' deve ter entre 300 a 1500 caracteres.")
        self.__description = description

    @property
    def address(self):
        return self.__adress
    
    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError("'adress' deve ser do tipo str.")
        self.__adress = address

    @property
    def daily_rate(self):
        return self.__daily_rate
    
    @daily_rate.setter
    def daily_rate(self, daily_rate):
        if not isinstance(daily_rate, (int, float)):
            raise TypeError("'daily_rate' deve ser do tipo float ou int.")
        self.__daily_rate = daily_rate

    @property
    def availability(self):
        return self.__availability
    
    @availability.setter
    def availability(self, availability):
        if not isinstance(availability, list):
            raise TypeError("'availability' deve ser uma lista.")
        
        validated_periods = []
        for period in availability:
            if not isinstance(period, dict):
                raise TypeError("Os elementos de 'availability' devem ser dicionários.")
            if "start" not in period or "end" not in period:
                raise ValueError("Dicionários de 'availability' devem conter as chaves 'start' e 'end'.")
            
            try:
                start_date = datetime.strptime(period["start"], "%Y-%m-%d").date()
                end_date = datetime.strptime(period["end"], "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("As datas devem estar no formato 'YYYY-MM-DD'")

            if start_date > end_date:
                raise ValueError("A data de início não pode ser depois da data de fim")
            
            validated_periods.append({
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            })

        self.__availability = validated_periods
    
    @property
    def owner_id(self):
        return self.__owner_id
    
    @owner_id.setter
    def owner_id(self, owner_id):
        self.__owner_id = owner_id

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "adress": self.address,
            "daily_rate": self.daily_rate,
            "availability": self.availability,
            "owner_id": self.owner_id,
            "id": self.id
        }