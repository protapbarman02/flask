from flask_smorest import Blueprint
from flask.views import MethodView

from app.db import db
from app.models import PhoneModel
from app.schemas import (
    PhoneSchema,
    PhoneUpdateSchema,
    PhoneOneFiendUpdateSchema,
    PhoneSearchSchema,
)


# initialize blueprint
phones_blp = Blueprint(
    "Phones",
    __name__,
    url_prefix="/phones",
    description="Phone APIs",
)


@phones_blp.route("/")
class PhoneControllers(MethodView):
    # get data
    @phones_blp.response(200, PhoneSchema(many=True))
    def get(self):
        return PhoneModel.query.all()

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
        phone = PhoneModel.query.get(update_phone_data["id"])
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
        phone = PhoneModel.query.get(id)
        phone.modelname = req["modelname"]
        phone.brand = req["brand"]
        phone.price = req["price"]
        phone.about = req["about"]
        phone.is_smart_phone = req["is_smart_phone"]
        db.session.commit()
        return phone


@phones_blp.route("/search")
class PhoneSearchSchema(MethodView):
    # find data
    @phones_blp.response(200, PhoneSchema(many=True))
    @phones_blp.arguments(PhoneSearchSchema, location="query")
    def get(self, args):
        id = args.get("id")
        qry = args.get("qry")

        phones = PhoneModel.query.all()
        if qry != None:
            phones = [
                phone for phone in phones if qry.lower() in phone.modelname.lower()
            ]
        if id != None:
            phones = [phone for phone in phones if phone.id == id]

        return phones
