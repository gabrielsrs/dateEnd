from flask_restx import Model, fields

class CustomField(fields.Raw):
    __schema_type__ = "string"
    __schema_example__ = "Africa/Johannesburg"

date_payload = Model('Date payload', {
    'title': fields.String(require=False),
    'date': fields.DateTime(require=False),
    'timezone': CustomField(require=False),
})

date_payload_models = [date_payload]
