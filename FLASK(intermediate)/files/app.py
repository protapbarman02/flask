from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_smorest import Blueprint, Api
from flask.views import MethodView

# 1. app
app = Flask(__name__)
app.config["API_TITLE"] = "students api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.0"
app.config["OPENAPI_URL_PREFIX"] = "/"

app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# 2. db
db = SQLAlchemy()


# 3. model
class StudentModel(db.Model):
    _tablename_ = "students"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)


# 4. bind app with db
db.init_app(app)

with app.app_context():
    db.create_all()


# 5. schema
class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)


# 6. resources
student_blp = Blueprint(
    "students",__name__, url_prefix="/students", description="Students"
)

@student_blp.route("/")
class StudentsResource(MethodView):
    @student_blp.response(200, StudentSchema(many=True))            # why many=false does not work
    def get(self):
        return StudentModel.query.all()

    @student_blp.arguments(StudentSchema)
    @student_blp.response(201, StudentSchema)
    def post(self, new_student_data):
        student = StudentModel(**new_student_data)
        db.session.add(student)
        db.session.commit()
        return student

# 7. create api using Api
api = Api(app)
api.register_blueprint(student_blp)