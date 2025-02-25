from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata
from werkzeug.exceptions import BadRequest, NotFound

class UpdateDateService:
    def update_date(self, req_data, current_data):
        if not [item for item in req_data.values() if item is not None]:
            raise BadRequest("Nothing to update")

        if not current_data:
            raise NotFound("Informed Id not return any registered date")

        date = req_data.copy()

        update_data = current_data.copy()
        update_data.pop("_id")

        if date["dateEnd"]:
            define_timezone = date['dateEnd'].replace(
                tzinfo=ZoneInfo(date["timezone"] or update_data["iana"])
            )
            date.pop("dateEnd")

            date["date_time_local"] = define_timezone.replace(tzinfo=None).isoformat()
            date["date_time_utc"] = define_timezone.astimezone(
                ZoneInfo('utc')).replace(tzinfo=None
            ).isoformat()

            date["iana"] = date.pop("timezone") or update_data["iana"]
            date["tzdb"] = tzdata.IANA_VERSION

        date["updated_at_utc"] = datetime.now(ZoneInfo('utc')).replace(tzinfo=None).isoformat()

        update_data.update({k: str(v) for k, v in date.items() if v is not None})

        return update_data
