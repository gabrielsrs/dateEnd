from datetime import datetime
from zoneinfo import ZoneInfo
import tzdata

class UpdateDateService:
    def update_date(self, update_parser, req_data, current_data):
        if not req_data:
            return {"message": "Nothing to update"}, 400
        elif not current_data:
            return {"message": "Informed Id not return any registered date"}, 400

        date = req_data.copy()
        date.update(update_parser().parse_args())

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
            date["tzdb"] = tzdata.__version__

        date["updated_at_utc"] = datetime.now(ZoneInfo('utc')).replace(tzinfo=None).isoformat()

        update_data.update({k: str(v) for k, v in date.items() if v is not None})

        return update_data
