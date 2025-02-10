from flask_restx import fields, Model

wild = fields.Wildcard(fields.Raw)
wildcard_fields_update = Model('Others(Update)', {
    '*': wild
})

raw_fields = Model('Base fields(Update)', {
    'id': fields.String,
    'title': fields.String,
    **wildcard_fields_update,
    'date_time_local': fields.DateTime(),
    'date_time_utc': fields.DateTime(),
    'iana': fields.String(),
    'tzdb': fields.String(),
    'updated_at_utc': fields.DateTime(),
})

updated_date = Model('Update Date', {
    'code': fields.Integer(default=200),
    'message': fields.String(default='Date successfully created'),
    'matched_count': fields.String(),
    'modified_count': fields.String(),
    'data': fields.Nested(raw_fields)
})

update_models = [wildcard_fields_update, raw_fields, updated_date]
