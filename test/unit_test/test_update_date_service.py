from dataclasses import asdict
from datetime import date

import pytest
from werkzeug.exceptions import BadRequest, NotFound

from ...src.services.update_date_service import UpdateDateService
from ..data_factories.date_factory import DateFactory
from ..data_factories.date_db_factory import DateDbFactory

update_date_service = UpdateDateService()

def test_update_date_structure():
    """Test date update to assert if service is formatting fields as expected"""
    date_object = DateFactory()
    date_object_from_db = DateDbFactory()
    update_date = update_date_service.update_date(asdict(date_object), asdict(date_object_from_db))

    assert date_object.title == update_date['title']
    assert date_object.dateEnd.isoformat() == update_date['date_time_local']
    assert date_object.timezone == update_date['iana']
    assert update_date['date_time_utc']
    assert update_date['tzdb']
    assert update_date['updated_at_utc']

def test_update_with_not_request_data():
    """Test date update without request data to assert error"""
    date_object = DateFactory(title=None, dateEnd=None, timezone=None)
    date_object_from_db = DateDbFactory()

    with pytest.raises(BadRequest) as excinfo:
        update_date_service.update_date(asdict(date_object), asdict(date_object_from_db))

    assert excinfo.type is BadRequest
    assert "Nothing to update" in str(excinfo.value)

def test_update_with_not_db_data():
    """Test date update without database corresponded object to assert error"""
    date_object = DateFactory()
    date_object_from_db = None

    with pytest.raises(NotFound) as excinfo:
        update_date_service.update_date(asdict(date_object), date_object_from_db)

    assert excinfo.type is NotFound
    assert "Informed Id not return any registered date" in str(excinfo.value)

def test_update_without_dateEnd():
    """Test date update without dateEnd and with other information to assert date format constancy"""
    date_object = DateFactory(dateEnd=None, timezone=None)
    date_object_from_db = DateDbFactory()

    update_date = update_date_service.update_date(asdict(date_object), asdict(date_object_from_db))

    assert date_object.title == update_date['title']
    assert date_object.dateEnd != update_date['date_time_local']
    assert date_object_from_db.date_time_utc == update_date['date_time_utc']
    assert date_object.timezone != update_date['iana']
    assert update_date['tzdb']
    assert date.today().isoformat() in update_date['updated_at_utc']
