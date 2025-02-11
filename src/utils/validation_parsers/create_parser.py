from flask_restx import reqparse, inputs
from .custom_types.tz_identifier import tz_identifier

class CreateParser:
    def __init__(self):
        self.create_parser = reqparse.RequestParser(bundle_errors=True, trim=True)

    def __call__(self):
        self.create_parser.add_argument('title', required=True, type=str, location='json')
        self.create_parser.add_argument('dateEnd', required=True, type=inputs.datetime_from_iso8601, location='json')
        self.create_parser.add_argument('timezone', required=True, type=tz_identifier, location='json')

        return self.create_parser
