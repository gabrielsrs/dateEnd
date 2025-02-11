from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata

class CreateDateService:   
    def create_date(self, req_data, create_parser):
        date = req_data.copy()
        date.update(create_parser().parse_args())

        define_timezone = date['dateEnd'].replace(tzinfo=ZoneInfo(date["timezone"]))
        date.pop("dateEnd")

        date["date_time_local"] = define_timezone.replace(tzinfo=None).isoformat()
        date["date_time_utc"] = define_timezone.astimezone(ZoneInfo('utc')).replace(tzinfo=None).isoformat()
        date["iana"] = date.pop("timezone")
        date["tzdb"] = tzdata.__version__
        date["updated_at_utc"] = datetime.now(ZoneInfo('utc')).replace(tzinfo=None).isoformat()

        return {k: str(v) for k, v in date.items()}
