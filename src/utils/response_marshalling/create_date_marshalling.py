from flask_restx import fields, Model

wild = fields.Wildcard(fields.Raw)
wildcard_fields_create = Model('Others(Create)', {
    '*': wild
})

raw_fields = Model('Base fields(Create)', {
    'id': fields.String,
    'title': fields.String,
    **wildcard_fields_create,
    'date_time_local': fields.DateTime(),
    'date_time_utc': fields.DateTime(),
    'iana': fields.String(),
    'tzdb': fields.String(),
    'updated_at_utc': fields.DateTime(),
})

created_date = Model('Created Date', {
    'code': fields.Integer(default=201),
    'message': fields.String(),
    'data': fields.Nested(raw_fields)
})

create_models = [wildcard_fields_create, raw_fields, created_date]