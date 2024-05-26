from flask import Flask, request
from marshmallow import Schema
from flask_smorest import Api, Blueprint
from flask.views import MethodView

app = Flask(__name__)
app.config["API_TITLE"] = "cars_api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"

# 17 Configuring the Swagger UI path and URL
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


s_bp = Blueprint("s_bp", __name__, url_prefix="/s")


s_schema = Schema()
s_schema.type = 'object'
s_schema.properties = {
    'name': {'type': 'string'}
}
s_schema.required = ['name']

@s_bp.route('/<int:id>', methods=['GET'])
class ABC(MethodView):
    @s_bp.response(200, s_schema)
    def get(self, id):
        return id



api = Api(app)

api.register_blueprint(s_bp)