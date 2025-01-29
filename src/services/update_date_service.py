from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata

class UpdateDateService:
    def update_date(self, update_parser, req_data, current_data):
        date = req_data.copy()
        date.update(update_parser().parse_args())

        update_data = current_data.copy()
        update_data.pop("_id")

        if date["dateEnd"]:
            define_timezone = date['dateEnd'].replace(tzinfo=ZoneInfo(date["timezone"] or update_data["iana"]))
            date.pop("dateEnd")

            date["dateTimeLocal"] = str(define_timezone.replace(tzinfo=None))
            date["dateTimeUTC"] = str(define_timezone.astimezone(ZoneInfo('utc')).replace(tzinfo=None))
            date["iana"] = date.pop("timezone") or update_data["iana"]
            date["tzdb"] = tzdata.__version__

        date["updatedAtUTC"] = str(datetime.now(ZoneInfo('utc')).replace(tzinfo=None))
        
        update_data.update({v is not None and k: str(v) for k, v in date.items()})
        update_data.pop(False)

        return update_data
