import mysql.connector
import csv, json
from decimal import Decimal
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
    
def print_tables2(conn, table):
    query = f"select * from {table}"
    cursor = conn.cursor()
    cursor.execute(query)
    columns_names = [i[0] for i in cursor.description]
    print("\t".join(columns_names))
    for row in cursor.fetchall():
            print("\t".join(str(cell) for cell in row))
    cursor.close()



def info(conn, table):        # Teste
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


def export_to_csv(conn, table):
    cursor = conn.cursor()

    
    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    
    column_names = [i[0] for i in cursor.description]

    
    with open('file.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(column_names)
        
        for row in cursor.fetchall():
            csvwriter.writerow(row)

    
    cursor.close()
    conn.close()

def export_to_json(conn, table):
    cursor = conn.cursor()

    
    query = f"SELECT * FROM {table}"
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
    close_connection(conn)

def close_connection(conn):
    conn.close()





def tree(conn):
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Banco de Dados MySQL:")
    for tabela in tabelas:
        print(f"|-- {tabela[0]}")
        cursor.execute(f"DESCRIBE {tabela[0]}")
        colunas = cursor.fetchall()
        for coluna in colunas:
            print(f"    |-- {coluna[0]}")
    cursor.close()


def imprimir_hierarquia_mysql(conexao):
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Banco de Dados MySQL:")
    for tabela in tabelas:
        print(f"|-- {tabela[0]}")
        cursor.execute(f"DESCRIBE {tabela[0]}")
        colunas = cursor.fetchall()
        for coluna in colunas:
            chave_primaria = ' (PK)' if coluna[3] == 'PRI' else ''
            print(f"    |-- {coluna[0]}{chave_primaria}")
    cursor.close()




def logo():
    hippo = """
             __
 
                  ,-.____,-.
                  /   ..    |
                 /_        _|
                |'o'      'o'|
               / ____________ |
             , ,'    `--'    '. .
            _| |              | |_
          /  ' '              ' '  |
         (    `,',__________.','    )
          \_    ` ._______, '     _/
             |                  |
             |    ,-.    ,-.    |
              \      ).,(      /
               \___/    \___/
                                
        """
    print(hippo)






def logo1():
    hippo = """

        HIPPO DB

 ⠀⠀⠀⠀⠀⠀⠀⠀⣞⠛⠓⢦⡀⠀⠀⠀⠀⢀⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡽⠟⠊⣩⠉⠑⢲⠞⡹⢊⣩⡇⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⠤⢤⠰⠁⣀⣀⠀⠀⢹⠿⠤⢤⣤⠶⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣴⠃⣿⣿⡿⠀⢸⣽⣷⡇⠀⠈⠣⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠖⠋⠉⠀⢀⡭⠋⠉⠛⠢⢄⡸⠿⠟⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀
⡼⠟⠱⠀⠀⢠⠋⠀⠀⠀⣠⡀⠀⠈⠑⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠸⡀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠛⠀⠀⠀⠀⠱⠿⠀⠀⠀⠀⣀⠠⠄⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⡇⠀⠀⠀⠀⠀⠀
⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀
⢹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡧⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣷⠀⠀⠀⠀⠀⠀
⠀⢯⣙⣲⠦⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⣸⡿⣤⡤⠤⢴⡶⣧
⠀⠀⠀⠀⠀⠀⠀⠉⠓⠲⣤⠤⠒⢲⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⢠⠇⠙⢿⣦⠄⣀⡴⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⢸⠀⠀⠀⠈⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡲⢄⡀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠉⠒⢤⣄⣀⠀⢱⠀⠀⠀⠀⠀⡇⠀⣀⣠⠴⠒⣿⠀⠀⠀⠀⠀⣸⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢹⠈⠉⢹⡀⠀⠀⠀⠀⣟⠉⠁⠀⠀⠀⠹⣆⡔⠢⣰⣒⡷⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡀⠀⠀⠀⠈⡇⠀⠸⡇⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠷⣋⡉⠦⠴⠃⠀⠀⡇⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣍⣷⣎⣩⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 
                                
        """
    print(hippo)
