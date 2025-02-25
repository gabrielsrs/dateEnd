from dataclasses import dataclass

@dataclass
class DateFromDb:
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
    class Meta:
        model = DateFromDb

    _id= LazyFunction(ObjectId)
    title= Faker('sentence')
    date_time_local= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
    date_time_utc= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
    tzdb= tzdata.IANA_VERSION
    iana= Faker('timezone')
    updated_at_utc= Transformer(Faker('date_time'), transform=lambda date: date.isoformat())
