from flask_restx import reqparse, inputs

class UpdateParser:
    def __call__(self, *args, **kwds):
        update_parser = reqparse.RequestParser(bundle_errors=True)
        update_parser.add_argument('title', required=False, type=str, location='json') #help='Must to have a title and be in string format', 
        update_parser.add_argument('dateEnd', required=False, type=inputs.datetime_from_iso8601, location='json') #help='Date is not valid, must be in ISO8601 format("2012-01-01T23:30:00+02:00")', 
        update_parser.add_argument('timezone', required=False, type=str, location='json')

        return update_parser