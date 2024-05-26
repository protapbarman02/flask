from flask_smorest import Blueprint
from app.db import db
from app.models import CarModel
from flask.views import MethodView
from app.schemas import (
    CarSchema,
    CarUpdateSchema,
    ColorUpdateSchema,
    ColorUpdateSchemaWithoutIdInBody,
    CarQuerySchema,
)

cars_blp = Blueprint("Cars", __name__, url_prefix="/cars", description="Car APIs")


@cars_blp.route("/")
class CarsController(MethodView):
    # get all cars
    @cars_blp.response(200, CarSchema(many=True))
    def get(self):
        return CarModel.query.all()

    # add a car
    @cars_blp.arguments(CarSchema)
    @cars_blp.response(201, CarSchema)
    def post(self, new_car):
        car = CarModel(**new_car)
        db.session.add(car)
        db.session.commit()
        return car

    # update a car(using id (follow car update schema))
    @cars_blp.arguments(CarUpdateSchema)
    @cars_blp.response(200, CarSchema)
    def put(self, update_car_data):
        car = CarModel.query.get(update_car_data["id"])
        car.brand = update_car_data["brand"]
        car.model = update_car_data["model"]
        car.price = update_car_data["price"]
        car.color = update_car_data["color"]
        db.session.commit()
        return car

    # update color of a car(using id (follow color update schema))
    @cars_blp.arguments(ColorUpdateSchema)
    @cars_blp.response(200, CarSchema)
    def patch(self, update_color_data):
        car = CarModel.query.get(update_color_data["id"])
        car.color = update_color_data["color"]
        db.session.commit()
        return car


# lets say id=1, for that
# request-url :   http://127.0.0.1:8000/cars/1
@cars_blp.route("/<int:id>")
class CarsControllerRouteParameters(MethodView):

    @cars_blp.response(200, CarSchema)
    def get(self, id):
        return CarModel.query.get(id)

    # updating color of a car using id
    # color is passed in body, id is in url parameter
    @cars_blp.arguments(ColorUpdateSchemaWithoutIdInBody)
    @cars_blp.response(200, CarSchema)
    def patch(self, update_color_data_without_id, id):
        # When using Flask-Smorest decorators like
        # @cars_blp.arguments(ColorUpdateSchemaWithoutId) to
        # specify additional parameters for a route,
        # those parameters should come before any
        # URL parameters in the method signature.
        car = CarModel.query.get(id)
        car.color = update_color_data_without_id["color"]
        db.session.commit()
        return car


# get cars based on model and or color
# get method can not have parameteres in (location)body
# but we are using it in the cars_blp.arguments(parameter)  for query,color
# thats why we explicitly set parameter location as query(any)
@cars_blp.route("/search")
class CarControllerByQuery(MethodView):
    # request-url :   http://127.0.0.1:8000/cars/search?qry=my_query
    @cars_blp.arguments(CarQuerySchema, location="query")
    @cars_blp.response(200, CarSchema(many=True))
    def get(self, query_data):
        # qry=query_data["qry"]     # raise key error if key not found
        qry = query_data.get("qry")  # returns None if key not found
        color = query_data.get("color")
        # cars=CarModel.query.filter(CarModel.model.like("%"+qry+"%")).all()
        cars = CarModel.query.all()
        if qry is not None:
            cars = [car for car in cars if qry.lower() in car.model.lower()]
        if color is not None:
            cars = [car for car in cars if color.lower() == car.color.lower()]
        return cars
