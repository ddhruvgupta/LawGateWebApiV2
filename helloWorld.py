from clients.databaseClient import DatabaseClient
from flask import Flask, request, jsonify
from controllers.clientController import client_blueprint

app = Flask(__name__)
app.register_blueprint(client_blueprint)

print(app.blueprints.keys())

# MySQL database configuration
# db_config = {
#     'user': 'root',
#     'password': 'Test123!',
#     'host': 'http://127.0.0.1:5000/',
#     'database': 'LawgateV2'
# }

@app.route('/', methods=['GET'])
def hello_world():
    # client = DatabaseClient()
    # result = client.fetch_all("SELECT * FROM clients")
    return jsonify(app.blueprints.keys())
    


# @app.route('/getContract', methods=['GET'])
# @app.route('/getLetter', methods=['GET'])
# def get_file():



# @app.route('/putContract', methods=['PUT'])
# @app.route('/putLetter', methods=['PUT'])
# def put_file():



if __name__ == '__main__':
    app.run(debug=True)
    