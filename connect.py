import mysql.connector
import psycopg2

def connect_to_database_psql():
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgres",
            database="template1",
            port="5433"
        )
        #if conn.is_connected():
        #    print("Conexão bem-sucedida")
        #    return conn
    except psycopg2.DatabaseError as err:
        print(f"Erro: {err}")
        return None

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="University"
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
    for row in results:
        print(row)
    cursor.close()

def close_connection(conn):
    conn.close()
