from flask import Flask
from app.db import db
from flask_smorest import Api
from app.controllers import cars_blp,phones_blp,students_blp
from flask_migrate import Migrate

def create_app():

    app = Flask(__name__)

    app.config["API_TITLE"] = "Simple Api"
    app.config["API_VERSION"] = "v2"
    app.config["OPENAPI_VERSION"] = "3.1.1"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///simple.db"
    
    migrate = Migrate(app, db)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    api = Api(app)
    api.register_blueprint(cars_blp)
    api.register_blueprint(phones_blp)
    api.register_blueprint(students_blp)

    return app