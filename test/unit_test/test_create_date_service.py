from dataclasses import asdict

from ...src.services.create_date_service import CreateDateService
from ..data_factories.date_factory import DateFactory

create_date_service = CreateDateService()

def test_create_date_structure():
    date_object = DateFactory()
    created_date = create_date_service.create_date(asdict(date_object))

    assert date_object.title == created_date['title']
    assert date_object.dateEnd.isoformat() == created_date['date_time_local']
    assert date_object.timezone == created_date['iana']
    assert created_date['date_time_utc']
    assert created_date['tzdb']
    assert created_date['updated_at_utc']
