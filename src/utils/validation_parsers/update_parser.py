from flask_restx import reqparse, inputs
from .custom_types.tz_identifier import tz_identifier

class UpdateParser:
    """Fields to validate when update date"""
    def __init__(self):
        """Initiate parser"""
        self.update_parser = reqparse.RequestParser(bundle_errors=True)

    def __call__(self, *args, **kwds):
        """
        Add fields in parser

        :return: A RequestParser object with created config
        """
        self.update_parser.add_argument('title', required=False, type=str, location='json')
        self.update_parser.add_argument('dateEnd', required=False, type=inputs.datetime_from_iso8601, location='json')
        self.update_parser.add_argument('timezone', required=False, type=tz_identifier, location='json')

        return self.update_parser