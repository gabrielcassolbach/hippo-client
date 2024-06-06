import mysql.connector
import psycopg2
import csv, json
from decimal import Decimal
from graphic_engine import print_line
from colorama import init, Fore, Back, Style

def connect_to_database_psql(connection_data):
    try: 
        conn2 = psycopg2.connector.connect(
            host = connection_data['host'],
            user = connection_data['user'],
            password = connection_data['password'],
            database = connection_data['database'],
            port = connection_data['port']
        )
        if(conn2.is_connected()):
            print("Conexão bem-sucedida")
            return conn2
    except psycopg2.Error as err:
        print(Fore.RED + f"Erro: {err}")
        print(Fore.CYAN)
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
        print(Fore.RED + f"Erro: {err}")
        print(Fore.CYAN)
        return None

def query_database(conn, query):
    if(query == ""): 
        print(Fore.RED + "invalid query")
        print(Fore.CYAN)
        return 0
    cursor = conn.cursor()
    try:
        cursor.execute(query) 
    except mysql.connector.Error as err:
        print(Fore.RED + "invalid query")
        print(Fore.CYAN)
        cursor.close()
        return 0
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    results = cursor.fetchall()
    print_tables(results, field_names)
    cursor.close()
    return 1

def print_tables(results, field_names):
    print(Fore.GREEN)
    for field in field_names:
        print("  | ", end = " ")
        print(field, end = "\t")
    print(Fore.CYAN)
    for row in results:
        for column in row:
            print("  | ", end = " ")
            print(column, end = "\t")
        print("")
    print("\n")

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
    val = query_database(conn, query)
    while val != 1: 
        query = input("\t type your query: ")
        val = query_database(conn, query)
    while True: 
        print("Do you to store your query data? \n")
        options = (input("\t -- 1 to export data to csv \n\t -- 2 to export data to json \n\t -- 3 to do nothing: \n"))
        match(options): 
            case "1":
                export_to_csv(conn, query)
                break        
            case "2":
                export_to_json(conn, query)
                break      
            case "3":
                break
            case _: 
                print(Fore.RED + "invalid input...")
                print(Fore.CYAN)
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
            column_type = column[1]
            primary_key = ' (PK)' if column[3] == 'PRI' else ''
            print(f"    |-- {column[0]}:{column_type}{primary_key}")
    cursor.close()