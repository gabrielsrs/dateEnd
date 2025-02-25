from dataclasses import dataclass
from datetime import datetime


@dataclass
class Date:
    title: str
    dateEnd: datetime
    timezone: str


from factory import Factory, Faker


class DateFactory(Factory):
    class Meta:
        model = Date

    title = Faker('sentence')
    dateEnd = Faker('date_time')
    timezone = Faker('timezone')
