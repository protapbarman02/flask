from marshmallow import fields, Schema
from app.schemas import StudentSchema
from app.schemas import PhoneSchema

class StudentWithPhonesInsideSchema(StudentSchema):
    phones=fields.List(fields.Nested('PhoneSchema'),dump_only=True)

class PhoneWithStudentInsideSchema(PhoneSchema):
    student=fields.Nested('StudentSchema', dump_only=True)

class ResponseSchema(Schema):
    response_code=fields.Integer(dump_only=True)
    message=fields.String(dump_only=True)

