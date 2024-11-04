from flask import Flask, request, jsonify
from endpoints.ClientEndpoint import client_blueprint
from endpoints.ContractEndpoint import contract_blueprint

app = Flask(__name__)
app.register_blueprint(client_blueprint)
app.register_blueprint(contract_blueprint)

print(app.blueprints.keys())

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(app.blueprints.keys())
    


if __name__ == '__main__':
    app.run(debug=True)
    