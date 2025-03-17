from dataclasses import dataclass
from datetime import datetime


@dataclass
class Date:
    """Object definition with requires fields"""
    title: str
    dateEnd: datetime
    timezone: str


from factory import Factory, Faker


class DateFactory(Factory):
    """Create factory related with date object"""
    class Meta:
        """Define the date object to be generated in factory """
        model = Date

    title = Faker('sentence')
    dateEnd = Faker('date_time')
    timezone = Faker('timezone')
