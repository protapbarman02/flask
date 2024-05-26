from app.schemas.car_schema import (
    CarSchema,
    CarUpdateSchema,
    ColorUpdateSchema,
    ColorUpdateSchemaWithoutIdInBody,
    CarQuerySchema,
)

from app.schemas.phone_schema import(
    PhoneSchema,
    PhoneUpdateSchema,
    PhoneOneFiendUpdateSchema,
    PhoneSearchSchema
)
from app.schemas.student_schema import(
    StudentSchema,
    UpdateStudentSchema,
    UpdateStudentPasswordSchema,
    StudentQuerySchema
)
from app.schemas.common_schema import(
    StudentWithPhonesInsideSchema,
    PhoneWithStudentInsideSchema,
    ResponseSchema
)