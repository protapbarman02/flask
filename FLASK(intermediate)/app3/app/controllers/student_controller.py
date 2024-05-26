from flask_smorest import Blueprint
from flask.views import MethodView

from app.db import db
from app.models import StudentModel
from app.schemas import (
    StudentSchema,
    UpdateStudentSchema,
    UpdateStudentPasswordSchema,
    StudentQuerySchema,
)

students_blp = Blueprint(
    "Students", __name__, url_prefix="/students", description="student APIs"
)


@students_blp.route("/")
class StudentsController(MethodView):

    @students_blp.response(200, StudentSchema(many=True))
    def get(self):
        return StudentModel.query.all()

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
        student = StudentModel.query.get(updated_student_data["id"])
        student.email = updated_student_data["email"]
        student.password = updated_student_data["password"]
        db.session.commit()
        return student


@students_blp.route("/<int:id>")
class StudentsController(MethodView):

    @students_blp.response(200, StudentSchema)
    def get(self, id):
        return StudentModel.query.get(id)

    @students_blp.response(200, StudentSchema)
    @students_blp.arguments(UpdateStudentPasswordSchema)
    def patch(self, req, id):
        student = StudentModel.query.get(id)
        student.password = req["password"]
        db.session.commit()
        return student


@students_blp.route("/search")
class StudentsControllerTres(MethodView):

    @students_blp.response(200, StudentSchema(many=True))
    @students_blp.arguments(StudentQuerySchema, location="query")
    def get(self, args):
        id = args.get("id")
        qry = args.get("qry")

        # students = StudentModel.query.filter(StudentModel.email.like("%" + qry + "%"))
        students = StudentModel.query.all()

        # search emails using the qry
        if qry != None:
            students = [
                student for student in students if qry.lower() in student.email.lower()
            ]

        # search ids using the id
        if id != None:
            students = [student for student in students if student.id == id]

        return students
