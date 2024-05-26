# # 1
# from flask import Flask
# # 3
# from flask_sqlalchemy import SQLAlchemy
# # 9
# from marshmallow import Schema, fields
# # 11
# from flask_smorest import Blueprint, Api
# # 13 
# from flask.views import MethodView
# # 2 creating Flask app
# app=Flask(__name__)
# # 4
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///cars.db"
# # 15
# app.config["API_TITLE"]="cars_api"
# app.config["API_VERSION"]="v1"
# app.config["OPENAPI_VERSION"]="3.1.0"
# app.config["OPENAPI_URL_PREFIX"]="/"

# # 17
# app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# # 5
# db=SQLAlchemy()
# # 6
# class CarModel(db.Model):
#     __tablename__="cars"
#     id=db.Column(db.Integer,primary_key=True)
#     brand=db.Column(db.String(50), nullable=False)
#     model=db.Column(db.String(50), nullable=False)
#     price=db.Column(db.Float, nullable=False)
#     color=db.Column(db.String(20),nullable=False)

# # 7
# db.init_app(app)
# # 8
# with app.app_context():
#     db.create_all()
# # 10
# class CarSchema(Schema):
#     id=fields.Integer(dump_only=True)
#     brand=fields.String(required=True)
#     model=fields.String(required=True)
#     price=fields.Float(required=True)
#     color=fields.String(required=True)

# # 12
# cars_bp= Blueprint("cars_bp_name",__name__,url_prefix="/cars")

# # 14
# @cars_bp.route("/")
# class CarsResource(MethodView):
#     @cars_bp.response(200,CarSchema(many=True))
#     def get(self):
#         return CarModel.query.all()

#     @cars_bp.arguments(CarSchema)
#     @cars_bp.response(201,CarSchema)
#     def post(self,new_car):
#         car=CarModel(**new_car)
#         db.session.add(car)
#         db.session.commit()
#         return car    
       
# # 16
# car_api=Api(app)
# car_api.register_blueprint(cars_bp)




# 1 Importing the Flask module
from flask import Flask

# 3 Importing SQLAlchemy for database operations
from flask_sqlalchemy import SQLAlchemy

# 9 Importing Marshmallow for data serialization and validation
from marshmallow import Schema, fields

# 11 Importing Blueprint and Api for building RESTful APIs
from flask_smorest import Blueprint, Api

# 13 Importing MethodView for defining views with explicit HTTP methods
from flask.views import MethodView

# 2 Creating a Flask app instance
app = Flask(__name__)

# 4 Configuring the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"

# 15 Configuring the API title, version, and OpenAPI settings
app.config["API_TITLE"] = "cars_api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"

# 17 Configuring the Swagger UI path and URL
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# 5 Creating a SQLAlchemy database instance
db = SQLAlchemy()

# 6 Defining a SQLAlchemy model for the 'cars' table
class CarModel(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)

# 7 binding SQLAlchemy object with the Flask app
db.init_app(app)

# 8 Creating all tables defined by SQLAlchemy models with context of app
with app.app_context():
    db.create_all()

# 10 Defining a Marshmallow schema for validating and serializing car data
class CarSchema(Schema):
    id = fields.Integer(dump_only=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    price = fields.Float(required=True)
    color = fields.String(required=True)

# 12 Creating a Blueprint for the car API endpoints
cars_bp = Blueprint("cars_bp_name", __name__, url_prefix="/cars")

# 14 Defining a resource class for handling car API endpoints
@cars_bp.route("/")
class CarsResource(MethodView):
    # Handling HTTP GET requests for retrieving car data
    @cars_bp.response(200, CarSchema(many=True))
    def get(self):
        return CarModel.query.all()

    # Handling HTTP POST requests for adding new car data by maintaining schema
    @cars_bp.arguments(CarSchema)
    @cars_bp.response(201, CarSchema)
    def post(self, new_car):
        car = CarModel(**new_car)
        db.session.add(car)
        db.session.commit()
        return car

# 16 Creating an Api instance and registering the Blueprint with it
car_api = Api(app)
car_api.register_blueprint(cars_bp)