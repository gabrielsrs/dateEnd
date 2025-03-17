from dataclasses import dataclass

@dataclass
class DateFromDb:
    """Object definition with requires fields"""
    _id: str
    title: str
    date_time_local: str
    date_time_utc: str
    tzdb: str
    iana: str
    updated_at_utc: str


import tzdata
from bson.objectid import ObjectId
from factory import Factory, Faker, LazyFunction, Transformer


class DateDbFactory(Factory):
    """Create factory related with date form database object"""
    class Meta:
        """Define the date object to be generated in factory """
        model = DateFromDb

    _id= LazyFunction(ObjectId)
    title= Faker('sentence')
    date_time_local= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
    date_time_utc= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
    tzdb= tzdata.IANA_VERSION
    iana= Faker('timezone')
    updated_at_utc= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
