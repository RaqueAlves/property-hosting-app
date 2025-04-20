from repository.property_repository import PropertyRepository
from repository.user_repository import UserRepository
from model.property import Property
from model.user_owner import UserOwner
from datetime import datetime, date

class PropertyService:

    def __init__(self, property_repository: PropertyRepository,
                 user_repository: UserRepository):
        self.repository = property_repository
        self.user_repository = user_repository

    def create_property(self, owner_id, title, description, address, daily_rate, availability):
        # Cria o imóvel
        new_property = Property(
            owner_id=owner_id,
            title=title,
            description=description,
            address=address,
            daily_rate=daily_rate,
            availability=availability
        )

        self.repository.add_property(new_property)
        return new_property

    def get_by_id(self, property_id):
        for property in self.repository.list_objects_properties():
            if property.id == property_id:
                return property
        return None

    def filter_properties(self, start=None, end=None, max_daily_rate=None, location=None):
        properties_filtered = []

        for property in self.repository.list_objects_properties():
            available = True

            if start and end:
                available = self.is_available(start, end, property)
            if not available:
                if max_daily_rate and property.daily_rate > max_daily_rate:
                    continue

                if location and location.lower() != property.address.lower():
                    continue

                properties_filtered.append(property)
        
        return properties_filtered

    def is_available(self, start, end, property: Property):
        if not isinstance(start, date):
            raise TypeError("Argumento 'start' deve ser do tipo date.")
        if not isinstance(end, date):
            raise TypeError("Argumento 'end' deve ser do tipo date.")

        for prop in property.availability:
            real_start = datetime.strptime(prop["start"], "%Y-%m-%d").date()
            real_end = datetime.strptime(prop["end"], "%Y-%m-%d").date()

            if start >= real_start and end <= real_end:
                return True
            
        return False