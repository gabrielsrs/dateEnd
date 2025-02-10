from flask_restx import fields, Model

status = Model('Status', ({
    'status': fields.String,
    'marker': fields.Integer
}))

datetime = Model('Datetime', {
    'years': fields.Integer,
    'months': fields.Integer,
    'weeks': fields.Integer,
    'days': fields.Integer,
    'hours': fields.Integer,
    'minutes': fields.Integer,
    'seconds': fields.Integer
})

max_unit = fields.Wildcard(fields.Integer)

wildcard_fields = Model('Max Unit', {
    '*': max_unit
})

absolute_datetime = Model('Absolute Datetime', {
    'max_unit': fields.Nested(wildcard_fields),
    **datetime
})

time_units = Model('Time Units', ({
    'datetime': fields.Nested(datetime),
    'absolute_datetime': fields.Nested(absolute_datetime),
}))

wild = fields.Wildcard(fields.Raw)
wildcard_fields_receive = Model('Others(Receive)', {
    '*': wild
})

raw_fields = Model('Base fields(Receive)', {
    'id': fields.String,
    'title': fields.String,
    **wildcard_fields_receive,
    'date_end_datetime': fields.DateTime(),
    'current_datetime': fields.DateTime(),
    'timezone': fields.String,
    'updated_at': fields.DateTime(),
    'status': fields.Nested(status),
    'time_units': fields.Nested(time_units),
})

get_date = Model('Receive date', {
    'code': fields.Integer,
    'message': fields.String(default='Date received'),
    'data': fields.Nested(raw_fields)
})

get_models = [
    get_date,
    raw_fields,
    time_units,
    absolute_datetime,
    wildcard_fields,
    wildcard_fields_receive,
    datetime,
    status
]
