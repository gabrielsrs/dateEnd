from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata

class CreateDateService:
    """Format dictionary for create date"""
    def create_date(self, req_data):
        """
        Formate a object from a given request data

        :param req_data: Request data with info to create date
        
        :return: Formatted date dictionary
        """
        date = req_data.copy()

        define_timezone = date['dateEnd'].replace(tzinfo=ZoneInfo(date["timezone"]))
        date.pop("dateEnd")

        date["date_time_local"] = define_timezone.replace(tzinfo=None).isoformat()
        date["date_time_utc"] = define_timezone.astimezone(ZoneInfo('utc')).replace(tzinfo=None).isoformat()
        date["iana"] = date.pop("timezone")
        date["tzdb"] = tzdata.IANA_VERSION
        date["updated_at_utc"] = datetime.now(ZoneInfo('utc')).replace(tzinfo=None).isoformat()

        return {k: str(v) for k, v in date.items()}
