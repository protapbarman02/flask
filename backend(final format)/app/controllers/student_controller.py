from flask_smorest import Blueprint
from flask.views import MethodView

from app.db import db
from app.models import StudentModel
from app.schemas import (
    StudentSchema,
    UpdateStudentSchema,
    UpdateStudentPasswordSchema,
    StudentQuerySchema
)
from app.schemas import(
    ResponseSchema
)

students_blp = Blueprint(
    "students", "students", url_prefix="/students", description="Students"
)


@students_blp.route("/")
class StudentsControllers(MethodView):

    # @students_blp.response(200, StudentSchema(many=True))
    # def get(self):
    #     return StudentModel.query.filter_by(status=1).all()

    @students_blp.response(200, StudentSchema(many=True))
    def get(self):
        return StudentModel.query.filter_by(status=1).all()

    @students_blp.response(201, StudentSchema)
    @students_blp.arguments(StudentSchema)
    def post(self, new_student_data):
        student = StudentModel(**new_student_data)
        db.session.add(student)
        db.session.commit()
        return student

    @students_blp.response(200, StudentSchema)
    @students_blp.arguments(UpdateStudentSchema)
    def put(self, updated_student_data):
        student = StudentModel.query.filter_by(id=updated_student_data["id"],status=1)
        student.email = updated_student_data["email"]
        student.password = updated_student_data["password"]
        db.session.commit()
        return student


@students_blp.route("/<int:id>")
class StudentsController(MethodView):

    @students_blp.response(200, StudentSchema)
    def get(self, id):
        return StudentModel.query.filter_by(id=id,status=1)

    @students_blp.response(200, StudentSchema)
    @students_blp.arguments(UpdateStudentPasswordSchema)
    def patch(self, req, id):
        student = StudentModel.query.filter_by(id=id,status=1)
        student.password = req["password"]
        db.session.commit()
        return student

    @students_blp.response(200,ResponseSchema)
    def delete(self,id):
        student=StudentModel.query.filter_by(id=id, status=1)
        if student is not None:
            student.status=0
            db.session.commit()
            return {
                "response code":200,
                "message":"successfully deleted Student"
                }
        return {
            "response code":204,
            "message":"no Student found"
            }


@students_blp.route("/search")     
class StudentControllerByQuery(MethodView):
    # request-url :   http://127.0.0.1:8000/cars/search?qry=my_query
    @students_blp.arguments(StudentQuerySchema,location="query")
    @students_blp.response(200, StudentSchema(many=True))
    def get(self,query_data):
        qry=query_data.get("qry")
        students=StudentModel.query.filter(
            (
                (StudentModel.name.like("%"+qry+"%")) | 
                (StudentModel.email.like("%"+qry+"%")) | 
                (StudentModel.program.like("%"+qry+"%"))
            ) & 
            (StudentModel.status==1)
        ).all()
        
        return students
