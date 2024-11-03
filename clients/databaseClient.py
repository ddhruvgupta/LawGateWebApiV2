import mysql.connector
from mysql.connector import Error


class DatabaseClient:
    def __init__(self, host='127.0.0.1', database='lawgateV2', user='root', password='Test123!'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.connect()

    def connect(self):
        print(self.host, self.database, self.user, self.password)

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySQL database")

    def fetch_all(self, query):
        if self.connection is None:
            print("Not connected to the database")
            return None
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_filtered(self, query, params):
        if self.connection is None:
            print("Not connected to the database")
            return None
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
        
    def insert(self, query, params):
        if self.connection is None:
            print("Not connected to the database")
            return None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Insert successful")
            print(cursor.lastrowid)
            return cursor.lastrowid
        except Error as e:
            print(f"Error: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

# # Example usage:
# if __name__ == "__main__":
#     client = DatabaseClient(database='lawgateV2', user='root', password='Test123!')
    
    
#     # Fetch all results
#     clients = client.fetch_all("SELECT * FROM Clients")
#     query = "INSERT INTO Clients (client_name, client_email, client_phone) VALUES (%s, %s, %s)"
#     params = ("test", "blah@gmail.com", "4047175785")
#     result = client.insert(query, params)
#     print(result)


#     clients = client.fetch_all("SELECT * FROM Clients")


#     client.disconnect()
#     # Fetch all clients
    
#     print("Clients:", clients)

    # Fetch all contracts
    # contracts = client.fetch_all("SELECT * FROM contracts")
    # print("Contracts:", contracts)

    # # Fetch all claims
    # claims = client.fetch_all("SELECT * FROM claims")
    # print("Claims:", claims)

    # # Fetch all letters
    # letters = client.fetch_all("SELECT * FROM letters")
    # print("Letters:", letters)

    # # Fetch all users
    # users = client.fetch_all("SELECT * FROM users")
    # print("Users:", users)

    # # Fetch filtered clients by name
    # filtered_clients = client.fetch_filtered("SELECT * FROM Clients WHERE client_name = %s", ('Sahu Construction',))
    # print("Filtered Clients:", filtered_clients)

    # # Fetch filtered contracts by client_id
    # filtered_contracts = client.fetch_filtered("SELECT * FROM contracts WHERE client_id = %s", (1,))
    # print("Filtered Contracts:", filtered_contracts)

    # # Fetch filtered claims by contract_id
    # filtered_claims = client.fetch_filtered("SELECT * FROM claims WHERE contract_id = %s", (1,))
    # print("Filtered Claims:", filtered_claims)

    # # Fetch filtered letters by contract_id
    # filtered_letters = client.fetch_filtered("SELECT * FROM letters WHERE contract_id = %s", (1,))
    # print("Filtered Letters:", filtered_letters)