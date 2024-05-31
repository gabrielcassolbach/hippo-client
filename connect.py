import mysql.connector
import psycopg2

def connect_to_database_psql(connection_data):
    try:
        conn2 = psycopg2.connect(
            host = connection_data['host'],
            user = connection_data['user'],
            password = connection_data['password'],
            database = connection_data['database'],
            port = connection_data['port']
        )
        return conn2
    except psycopg2.DatabaseError as err:
        print(f"Erro: {err}")
        return None

def connect_to_database(connection_data):
    try:
        conn = mysql.connector.connect(
            host = connection_data['host'],
            user = connection_data['user'],
            password = connection_data['password'],
            database = connection_data['database'],
            port = connection_data['port']
        )
        if conn.is_connected():
            print("Conexão bem-sucedida")
            return conn
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None

def query_database(conn, query):
    cursor = conn.cursor()
    print(cursor)
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    
def execute_mysql_query(conn):
    query = input("Digite sua consulta SQL:")
    query_database(conn, query)
    close_connection(conn)

def close_connection(conn):
    conn.close()
