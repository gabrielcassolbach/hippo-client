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
    cursor.execute(query)
    results = cursor.fetchall()
    print_tables(results)
    cursor.close()

def print_line(size):
    for i in range(1, int(size)):
        print("--", end="")
    print("")

def print_tables(results):
    print_line(25)
    for row in results:
        for column in row:
            print("  | ", end = " ")
            print(column, end = "\t")
        print("")
    print_line(25)
    
def execute_mysql_query(conn):
    query = input("\t type your query: ")
    query_database(conn, query)
    close_connection(conn)

def close_connection(conn):
    conn.close()
