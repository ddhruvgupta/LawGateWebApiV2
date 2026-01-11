from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_smorest import Api
from app.Controllers.ClientController import client_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configure Flask-Smorest OpenAPI settings
    app.config["API_TITLE"] = "LawGate API"
    app.config["API_VERSION"] = "1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-Smorest API
    api = Api(app)

    # Register blueprints
    api.register_blueprint(client_bp, url_prefix="/clients")

    @app.route("/")
    def index():
        return jsonify(list(app.blueprints.keys()))  

    return app
