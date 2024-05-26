from marshmallow import Schema, fields


class PlainPhoneSchema(Schema):
    id = fields.Integer(dump_only=True)
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)


class PlainStudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class StudentSchema(PlainStudentSchema):
    phones = fields.List(fields.Nested(PlainPhoneSchema()), dump_only=True)


class UpdateStudentSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UpdateStudentPasswordSchema(Schema):
    password = fields.String(required=True)


class StudentQuerySchema(Schema):
    id = fields.Integer(required=False)
    qry = fields.String(required=True)
