from flask import Flask
from flask_smorest import Api

from app.db import db
from app.resources import student_blp


def create_app():

    app = Flask(__name__)
    app.config["API_TITLE"] = "students api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.0"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

    # bind app with db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # create api using Api
    api = Api(app)
    api.register_blueprint(student_blp)

    return app
