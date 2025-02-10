from flask_restx import fields, Model

deleted_date = Model('Deleted Date', {
    'code': fields.Integer(default=200),
    'message': fields.String(default='Date deleted successfully')
})

delete_models = [deleted_date]
