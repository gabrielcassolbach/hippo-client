import mysql.connector
import csv, json
from decimal import Decimal
from graphic_engine import print_line
from colorama import init, Fore, Back, Style
#import psycopg2

#def connect_to_database_psql(connection_data):
#    try:
#        conn2 = psycopg2.connect(
#            host = connection_data['host'],
#            user = connection_data['user'],
#            password = connection_data['password'],
#            database = connection_data['database'],
#            port = connection_data['port']
#        )
#        return conn2
#    except psycopg2.DatabaseError as err:
#        print(f"Erro: {err}")
#        return None

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
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    results = cursor.fetchall()
    print_tables(results, field_names)
    #print_tables2(conn, query)
    #info(conn, "classroom")
    cursor.close()

def print_tables(results, field_names):
    print(Fore.RED)
    for field in field_names:
        print("  | ", end = " ")
        print(field, end = "\t")
    print(Fore.CYAN)
    for row in results:
        for column in row:
            print("  | ", end = " ")
            print(column, end = "\t")
        print("")
    print_line(len(results))

def info(conn, table):        
    cursor = conn.cursor()
    query = (
        "SELECT COLUMN_NAME, COLUMN_TYPE "
        "FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s"
    )
    cursor.execute(query, ('University', table))
    print("Column Name\tData Type")
    print("---------------------------")
    for row in cursor.fetchall():
        column_name = row[0]
        data_type = row[1]
        print(f"{column_name}\t{data_type}")
    
    cursor.close()
    conn.close()


def export_to_csv(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description]
    with open('file.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(column_names)
        for row in cursor.fetchall():
            csvwriter.writerow(row)
    cursor.close()
    conn.close()

def export_to_json(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description]
    data = []
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        for key in row_dict:
            if isinstance(row_dict[key], Decimal):
                row_dict[key] = str(row_dict[key])
        data.append(row_dict)
    with open('file.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    cursor.close()
    conn.close()


def execute_mysql_query(conn):
    query = input("\t type your query: ")
    query_database(conn, query)
    while True: 
        options = int(input("\t type 1 to export data to csv \n\t type 2 to export data to json \n\t type 3 to do nothing: \n"))
        if(options == 1): 
            export_to_csv(conn, query)
            break        
        if(options == 2):
            export_to_json(conn, query)
            break      
        if(options == 3):
            print("Leaving...")
            break
    close_connection(conn)

def close_connection(conn):
    conn.close()

def tree_new(conn):
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Databases: ")
    for table in tables:
        print(f"|-- {table[0]}")
        cursor.execute(f"DESCRIBE {table[0]}")
        columns = cursor.fetchall()
        for column in columns:
            primary_key = ' (PK)' if column[3] == 'PRI' else ''
            print(f"    |-- {column[0]}{primary_key}")
    cursor.close()