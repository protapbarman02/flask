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
from app.schemas import(
    # StudentWithPhonesInsideSchema,
    ResponseSchema
)
cars_blp = Blueprint("cars", __name__, url_prefix="/cars",description="Super Cars Lol")

@cars_blp.route("/")
class CarsController(MethodView):
    # get all cars
    @cars_blp.response(200, CarSchema(many=True))
    def get(self):
        return CarModel.query.filter_by(status=1).all()

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
    @cars_blp.response(200,CarSchema)
    def put(self,update_car_data):
        #car=CarModel.query.get(update_car_data["id"])
        car=CarModel.query.filter_by(id=update_car_data["id"],status=1).first()
        car.brand=update_car_data["brand"]
        car.model=update_car_data["model"]
        car.price=update_car_data["price"]
        car.color=update_car_data["color"]
        db.session.commit()
        return car

    # update color of a car(using id (follow color update schema))
    @cars_blp.arguments(ColorUpdateSchema)
    @cars_blp.response(200,CarSchema)
    def patch(self,update_color_data):
        car=CarModel.query.filter_by(id=update_color_data["id"],status=1)
        car.color=update_color_data["color"]
        db.session.commit()
        return car
    

# lets say id=1, for that
# request-url :   http://127.0.0.1:8000/cars/1
@cars_blp.route("/<int:id>")
class CarsControllerRouteParameters(MethodView):
    
    @cars_blp.response(200,CarSchema)
    def get(self,id):
        return CarModel.query.filter_by(id=id,status=1)

    # updating color of a car using id
    # color is passed in body, id is in url parameter
    @cars_blp.arguments(ColorUpdateSchemaWithoutIdInBody)
    @cars_blp.response(200,CarSchema)
    def patch(self,update_color_data_without_id,id):
        # When using Flask-Smorest decorators like 
        # @cars_blp.arguments(ColorUpdateSchemaWithoutId) to 
        # specify additional parameters for a route, 
        # those parameters should come before any 
        # URL parameters in the method signature.
        # car=CarModel.query.get(id)
        car=CarModel.query.filter_by(id=id,status=1)
        car.color=update_color_data_without_id["color"]
        db.session.commit()
        return car
    
    #permanently delete
    # @cars_blp.response(200)
    # def delete(self,id):
    #     car=CarModel.query.filter_by(id=id).first()
    #     if car is not None:
    #         db.session.delete(car)
    #         db.session.commit()
    #         return "successfully deleted(totally)"
    #     return "no car found"
    
    #indirectly delete
    @cars_blp.response(200,ResponseSchema)
    def delete(self,id):
        car=CarModel.query.filter_by(id=id, status=1).first()
        # car=CarModel.query.filter_by((CarModel.id==id) & (CarModel.status==1)).first()
        if car is not None:
            car.status=0
            db.session.commit()
            return {
                "response code":200,
                "message":"successfully deleted Car"
                }
        return {
            "response code":204,
            "message":"no Car found"
            }
        

# get cars based on model and or color 
# get method can not have parameteres in (location)body
# but we are using it in the cars_blp.arguments(parameter)  for query,color
# thats why we explicitly set parameter location as query(any)
@cars_blp.route("/search")     
class CarControllerByQuery(MethodView):
    # request-url :   http://127.0.0.1:8000/cars/search?qry=my_query
    @cars_blp.arguments(CarQuerySchema,location="query")
    @cars_blp.response(200, CarSchema(many=True))
    def get(self,query_data):
        qry=query_data.get("qry")
        cars=CarModel.query.filter(
            (
                (CarModel.brand.like("%"+qry+"%")) | 
                (CarModel.model.like("%"+qry+"%")) | 
                (CarModel.color.like("%"+qry+"%"))
            ) & 
            (CarModel.status==1)
        ).all()
        
        return cars