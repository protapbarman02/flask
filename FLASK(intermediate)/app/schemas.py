from marshmallow import Schema, fields


class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UpdateStudentSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UpdateStudentPasswordSchema(Schema):
    password = fields.String(required=True)


class StudentQuerySchema(Schema):
    id = fields.Integer(required=False)
    qry = fields.String(required=True)
