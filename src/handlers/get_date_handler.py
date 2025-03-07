from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser
from datetime import datetime
from zoneinfo import ZoneInfo
from aniso8601 import parse_datetime
from math import ceil
from werkzeug.exceptions import NotFound

class GetDateHandler:
    """Manage get request from a date"""

    def __init__(self, date_id):
        """Initiate the db connection, id to get date and a dictionary with seconds from time units"""

        self.conn = DateRepository()
        self.id = IdParser(date_id)

        self.time_units_in_seconds = {
            "seconds": 1, # second
            "minutes": 60, # 60 seconds
            "hours": 3600, # 60 min
            "days": 86400, # 24 hours
            "weeks": 604800, # 7 days
            "months": 2592000, # 30 days
            "years": 31536000 # 365 days
        }

    def get_date(self):
        """
        Query a date based in current class id

        :raise NotFound: Query from given id return nothing

        :return: A date object with additional informative fields
        """

        query_response = self.conn.find_one(self.id.id_to_object())

        if not query_response:
            raise NotFound("Id not found")

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        """
        Formate the query_response, and add some informative fields

        :param query_response: Database data from a given date id

        :return: Formatted date object response
        """

        formatted_data = query_response.copy()

        current_utc_time = datetime.now(
            ZoneInfo(formatted_data["iana"])
        ).replace(tzinfo=None)
        end_date = parse_datetime(formatted_data["date_time_local"])
        diff_in_secs = (end_date - current_utc_time).total_seconds()

        formatted_data["date_end_datetime"] = end_date.astimezone(
            ZoneInfo(formatted_data["iana"])
        ).isoformat(timespec="seconds")

        formatted_data["current_datetime"] = current_utc_time.astimezone(
            ZoneInfo(formatted_data["iana"])
        ).isoformat(timespec="seconds")

        formatted_data["timezone"] = formatted_data.pop("iana")

        formatted_data["updated_at"] = parse_datetime(
            formatted_data['updated_at_utc']
        ).astimezone(
            ZoneInfo(formatted_data["timezone"])
        ).isoformat(timespec="seconds")

        formatted_data.pop("_id")
        formatted_data.pop("date_time_local")
        formatted_data.pop("date_time_utc")
        formatted_data.pop("updated_at_utc")
        formatted_data.pop("tzdb")

        date = {
            "datetime": self._create_date(diff_in_secs),
            "absolute_datetime": self._create_absolute_date(diff_in_secs)
        }
        status = self._status(diff_in_secs)

        return {
            "code": 200,
            "data": {
                **self.id.object_to_id(),
                **formatted_data,
                "status": status,
                "time_units": date
            }
        }

    def _create_date(self, seconds):
        """
        Calculate the date based on seconds

        :param seconds: Seconds that represent a difference between to times

        :return: Date corresponding from the given seconds
        """

        date_for_end = {unit: 0 for unit in reversed(self.time_units_in_seconds)}

        for unit in  date_for_end:
            convert = divmod(abs(seconds), self.time_units_in_seconds[unit])

            seconds = convert[1]
            date_for_end[unit] = ceil(convert[0])

        return date_for_end

    def _create_absolute_date(self, seconds):
        """
        Calculate absolute seconds from each unit, since the total seconds correspond to a unit

        :param seconds: Seconds that represent a difference between to times

        :return: Absolute seconds from each unit
        """

        units_from_date = {unit: 0 for unit in reversed(self.time_units_in_seconds)}
        time_units_as_list = list(self.time_units_in_seconds)

        for unit, unit_values in self.time_units_in_seconds.items():
            convert = ceil(divmod(abs(seconds), unit_values)[0])

            if not convert:
                previous_value = time_units_as_list[time_units_as_list.index(unit) - 1]

                return {
                    "max_unit": {previous_value: units_from_date[previous_value]}, 
                    **units_from_date
                }

            if unit == time_units_as_list[-1]:
                units_from_date[unit] = convert

                return {
                    "max_unit": {unit: convert}, 
                    **units_from_date
                }

            units_from_date[unit] = convert

        return {}

    def _status(self, seconds):
        """
        Validate if the date has passed or not.

        :param seconds: Seconds that represent a difference between to times

        :return: Status object information if date end passed
        """

        if seconds > 0:
            return {"status": "Upcoming", "marker": 1}

        return {"status": "Finished", "marker": 0}
