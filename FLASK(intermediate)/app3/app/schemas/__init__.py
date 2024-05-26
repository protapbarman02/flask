# student schemas
from app.schemas.student_schema import StudentSchema
from app.schemas.student_schema import UpdateStudentSchema
from app.schemas.student_schema import UpdateStudentPasswordSchema
from app.schemas.student_schema import StudentQuerySchema

# car schemas
from app.schemas.car_schema import CarSchema
from app.schemas.car_schema import CarUpdateSchema
from app.schemas.car_schema import ColorUpdateSchema
from app.schemas.car_schema import ColorUpdateSchemaWithoutIdInBody
from app.schemas.car_schema import CarQuerySchema

# phone schemas
from app.schemas.phone_schema import PhoneSchema
from app.schemas.phone_schema import PhoneUpdateSchema
from app.schemas.phone_schema import PhoneOneFiendUpdateSchema
from app.schemas.phone_schema import PhoneSearchSchema
