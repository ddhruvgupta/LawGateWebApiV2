from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.Controllers.ClientController import client_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints, etc.
    app.register_blueprint(client_bp)

    @app.route("/")
    def index():
        return jsonify(list(app.blueprints.keys()))  

    return app
