from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata

class CreateDateService:   
    def create_date(self, req_data, create_parser):
        date = req_data.copy()
        date.update(create_parser().parse_args())

        define_timezone = date['dateEnd'].replace(tzinfo=ZoneInfo(date["timezone"]))
        date.pop("dateEnd")

        date["dateTimeLocal"] = str(define_timezone.replace(tzinfo=None))
        date["dateTimeUTC"] = str(define_timezone.astimezone(ZoneInfo('utc')).replace(tzinfo=None))
        date["iana"] = date.pop("timezone")
        date["tzdb"] = tzdata.__version__
        date["updatedAtUTC"] = str(datetime.now(ZoneInfo('utc')).replace(tzinfo=None))

        return {k: str(v) for k, v in date.items()}
