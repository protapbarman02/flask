from marshmallow import Schema, fields


class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    program = fields.String(required=True)
    status=fields.Integer(required=False,default=1, missing=1)

    from app.schemas.phone_schema import PhoneSchema
    phones = fields.List(fields.Nested(PhoneSchema), dump_only=True, exclude=("student",))


class UpdateStudentSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UpdateStudentPasswordSchema(Schema):
    password = fields.String(required=True)


class StudentQuerySchema(Schema):
    qry = fields.String(required=True)
