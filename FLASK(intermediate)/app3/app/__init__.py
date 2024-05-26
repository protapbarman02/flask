from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from app.db import db

from app.controllers import students_blp
from app.controllers import cars_blp
from app.controllers import phones_blp


def create_app():

    app = Flask(__name__)
    app.config["API_TITLE"] = "simple api"
    app.config["API_VERSION"] = "v3"
    app.config["OPENAPI_VERSION"] = "3.1.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

    # bind app with db
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    # create api using Api
    api = Api(app)
    api.register_blueprint(students_blp)
    api.register_blueprint(cars_blp)
    api.register_blueprint(phones_blp)

    return app
