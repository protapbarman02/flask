from flask_smorest import Blueprint
from flask.views import MethodView

from app.db import db
from app.models import PhoneModel
from app.schemas import (PhoneSchema,
    PhoneUpdateSchema,
    PhoneOneFiendUpdateSchema,
    PhoneSearchSchema
)
from app.schemas import(
    ResponseSchema
)

# initialize blueprint
phones_blp = Blueprint(
    "phones","phones",url_prefix="/phones",description="Phones",
)



@phones_blp.route("/")
class PhoneControllers(MethodView):
    # get data
    # @phones_blp.response(200, PhoneSchema(many=True))
    # def get(self):
    #     return PhoneModel.query.filter_by(status=1).all()

    @phones_blp.response(200, PhoneSchema(many=True))
    def get(self):
        return PhoneModel.query.filter_by(status=1).all()

    # submit data/create
    @phones_blp.response(201, PhoneSchema)
    @phones_blp.arguments(PhoneSchema)
    def post(self, new_phone_data):
        phone = PhoneModel(**new_phone_data)
        db.session.add(phone)
        db.session.commit()
        return phone

    # update data
    @phones_blp.response(200, PhoneSchema(many=False))
    @phones_blp.arguments(PhoneUpdateSchema)
    def put(self, update_phone_data):
        phone = PhoneModel.query.filter_by(id=update_phone_data["id"],status=1)
        phone.modelname = update_phone_data["modelname"]
        phone.brand = update_phone_data["brand"]
        phone.price = update_phone_data["price"]
        phone.about = update_phone_data["about"]
        phone.is_smart_phone = update_phone_data["is_smart_phone"]
        db.session.commit()
        return phone

@phones_blp.route("/<int:id>")
class PhoneController(MethodView):
    # update spacific field data
    @phones_blp.response(200, PhoneSchema)
    @phones_blp.arguments(PhoneOneFiendUpdateSchema)
    def patch(self, req, id):
        phone = PhoneModel.query.filter_by(id=id,status=1)
        phone.modelname = req["modelname"]
        phone.brand = req["brand"]
        phone.price = req["price"]
        phone.about = req["about"]
        phone.is_smart_phone = req["is_smart_phone"]
        db.session.commit()
        return phone

    @phones_blp.response(200,ResponseSchema)
    def delete(self,id):
        phone=PhoneModel.query.filter_by(id=id, status=1).first()
        if phone is not None:
            phone.status=0
            db.session.commit()
            return {
                "response code":200,
                "message":"successfully deleted Phone"
                }
        return {
            "response code":204,
            "message":"no Phone found"
            }

@phones_blp.route("/search")     
class PhoneControllerByQuery(MethodView):
    # request-url :   http://127.0.0.1:8000/phones/search?qry=my_query
    @phones_blp.arguments(PhoneSearchSchema,location="query")
    @phones_blp.response(200, PhoneSchema(many=True))
    def get(self,query_data):
        qry=query_data.get("qry")
        phones=PhoneModel.query.filter(
            (
                (PhoneModel.brand.like("%"+qry+"%")) | 
                (PhoneModel.modelname.like("%"+qry+"%")) | 
                (PhoneModel.about.like("%"+qry+"%"))
            ) & 
            (PhoneModel.status==1)
        ).all()
        
        return phones