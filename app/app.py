import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import icecream as ic

from Controllers.ClientController import client_bp
# from Controllers.ContractController import contract_blueprint

# Core Flask config

app = Flask(__name__)

# Core DB config
print(os.getenv("DATABASE_URL"))

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Optional pool tuning from env
# app.config["SQLALCHEMY_POOL_SIZE"] = int(os.getenv("SQLALCHEMY_POOL_SIZE", 5))
# app.config["SQLALCHEMY_MAX_OVERFLOW"] = int(os.getenv("SQLALCHEMY_MAX_OVERFLOW", 10))
# app.config["SQLALCHEMY_POOL_TIMEOUT"] = int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 30))
# app.config["SQLALCHEMY_POOL_RECYCLE"] = int(os.getenv("SQLALCHEMY_POOL_RECYCLE", 1800))
# app.config["SQLALCHEMY_POOL_PRE_PING"] = os.getenv("SQLALCHEMY_POOL_PRE_PING", "True").lower() == "true"


app.register_blueprint(client_bp)
# app.register_blueprint(contract_blueprint)

db = SQLAlchemy(app)

print(app.blueprints.keys())

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(list(app.blueprints.keys()))  


if __name__ == '__main__':
    app.run(debug=True)
    