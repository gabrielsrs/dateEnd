from zoneinfo import ZoneInfo, available_timezones
import datetime
import tzdata

class TimezonesHandler:
    """Menage get timezones available"""

    def timezones(self):
        """
        Get all currents available timezones

        :return: Information from tzdata from each timezone
        """

        timezones = []

        for tz_identifier in available_timezones():
            utc_offset = datetime.datetime.now(ZoneInfo(tz_identifier)).strftime('%z')

            timezones.append({"tz_identifier": tz_identifier, "utc_offset": utc_offset})

        timezones.sort(key=lambda x: x["utc_offset"])

        return {
            "code": 200,
            "message": "tz identifier and utc offset list",
            "tzdb": tzdata.__version__,
            "data": timezones
        }
