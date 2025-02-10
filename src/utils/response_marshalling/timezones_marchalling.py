from flask_restx import fields, Model

options = Model('Each Timezone', {
    'tz_identifier': fields.String(),
    'utc_offset': fields.String()
})

timezones = Model('Timezones Options', {
    'code': fields.Integer(default=200),
    'message': fields.String(),
    'tzdb': fields.String(),
    'data': fields.List(fields.Nested(options))
})

timezones_models = [timezones, options]
