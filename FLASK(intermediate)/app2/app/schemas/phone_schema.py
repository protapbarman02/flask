from marshmallow import Schema, fields


class PlainStudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class PlainPhoneSchema(Schema):
    id = fields.Integer(dump_only=True)
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)


# phone schema
class PhoneSchema(PlainPhoneSchema):
    student = fields.Nested(PlainStudentSchema(), dump_only=True)


# phone schema for update
class PhoneUpdateSchema(Schema):
    id = fields.Integer(required=True)
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)


# phone schema for single data/field
class PhoneOneFiendUpdateSchema(Schema):
    modelname = fields.String(required=True)
    brand = fields.String(required=True)
    price = fields.Float(required=True)
    about = fields.String(required=False)
    is_smart_phone = fields.Boolean(default=True)


# phone schema find-data
class PhoneSearchSchema(Schema):
    id = fields.Integer(required=False)
    qry = fields.String(required=True)
