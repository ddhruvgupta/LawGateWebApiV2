from controllers.databaseClient import DatabaseClient
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',
    'password': 'Test123!',
    'host': 'http://127.0.0.1:5000/',
    'database': 'LawgateV2'
}

@app.route('/', methods=['GET'])
def hello_world():
    client = DatabaseClient()
    result = client.fetch_all("SELECT * FROM clients")
    return jsonify(result)
    

# @app.route('/getContract', methods=['GET'])
# @app.route('/getLetter', methods=['GET'])
# def get_file():



# @app.route('/putContract', methods=['PUT'])
# @app.route('/putLetter', methods=['PUT'])
# def put_file():



if __name__ == '__main__':
    app.run(debug=True)
    