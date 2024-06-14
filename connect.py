import mysql.connector
import psycopg2
import csv, json
from decimal import Decimal
from graphic_engine import print_line
from colorama import init, Fore, Back, Style
from tabulate import tabulate
import os

def connect_to_database_psql(connection_data):
    try: 
        conn2 = psycopg2.connect(
            host = connection_data['host'],
            user = connection_data['user'],
            password = connection_data['password'],
            database = connection_data['database'],
            port = connection_data['port']
        )
        if(conn2):
            print("Conexão bem-sucedida")
            return conn2
    except psycopg2.Error as err:
        print(Fore.RED + f"Erro: {err}")
        print(Fore.CYAN)
        return None

def connect_to_database(connection_data):
    print("connecting to database...")
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
        if(err):
            print(Fore.RED + f"Erro: {err}")
            print(Fore.CYAN)
            return None
        else:
            raise
            return None

def query_database(conn, query, size, choice):
    if(query == ""): 
        print(Fore.RED + "invalid query")
        print(Fore.CYAN)
        return 0
    cursor = conn.cursor()
    if(choice == "psql"):
        try: 
            cursor.execute(query) 
        except psycopg2.Error as err:
            print(Fore.RED + f"Erro: {err}")
            print(Fore.CYAN)
            return None
    else:
        try: 
            cursor.execute(query) 
        except mysql.connector.Error as err:
            print(Fore.RED + f"Erro: {err}")
            print(Fore.CYAN)
            return None
    field_names = [i[0] for i in cursor.description]
    results = cursor.fetchall()
    formated_results = []
    counter = 1
    for result in results:
        if(counter <= size):
            formated_results.append(result) 
        counter = counter + 1
    if(size > 0):
        print_tables(formated_results, field_names)
    else: 
        print_tables(results, field_names)
    cursor.close()
    return 1

def print_tables(results, field_names):
    print(tabulate(results, headers=field_names, tablefmt="pretty"))
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

def execute_query(conn, choice):
    while True: 
        try:
            print("\t Select how many lines of the query result you want to see: ")
            print("\t 0 - To see the full result. ")
            print("\t A number between 1 to 1000 - To see a partial result. \n")
            size = int(input("\t Select: "))
            if(size >= 0 and size <= 1000):
                break
            else:
                print("invalid input...")
        except ValueError as err:
            print(Fore.RED + f"Erro: {err}")
            print(Fore.CYAN)

    os.system("clear")
    query = input("\t type your query: ")
    val = query_database(conn, query, size, choice)
    while val != 1: 
        query = input("\t type your query: ")
        val = query_database(conn, query, size, choice)
    while True: 
        print("Do you want to store your query data? \n")
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

def tree_psql(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tabelas = cursor.fetchall()
        print("Database:")
        for tabela in tabelas:
            print(Fore.RED + f"|-- {tabela[0]}" + Fore.CYAN)
            cursor.execute(f"""
                SELECT column_name, data_type, character_maximum_length,
                       (SELECT EXISTS (
                           SELECT 1 
                           FROM information_schema.table_constraints tc 
                           JOIN information_schema.key_column_usage kcu 
                           ON tc.constraint_name = kcu.constraint_name 
                           AND tc.table_schema = kcu.table_schema 
                           WHERE tc.constraint_type = 'PRIMARY KEY' 
                           AND tc.table_name = '{tabela[0]}' 
                           AND kcu.column_name = c.column_name
                       )) AS is_primary
                FROM information_schema.columns c 
                WHERE table_name = '{tabela[0]}' 
                AND table_schema = 'public'
            """)
            colunas = cursor.fetchall()
            for coluna in colunas:
                chave_primaria = ' (PK)' if coluna[3] else ''
                tipo_coluna = f"{coluna[1]}({coluna[2]})" if coluna[2] else coluna[1]
                print(f"    |-- {coluna[0]}: {tipo_coluna}{chave_primaria}")
        cursor.close()

def tree_new(conn):
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Database: ")
    for table in tables:
        print(Fore.RED + f"|-- {table[0]}" + Fore.CYAN) 
        cursor.execute(f"DESCRIBE {table[0]}")
        columns = cursor.fetchall()
        for column in columns:
            column_type = column[1]
            primary_key = ' (PK)' if column[3] == 'PRI' else ''
            print(f"    |-- {column[0]}:{column_type}{primary_key}")
    cursor.close()