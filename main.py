from connect import *
from graphic_engine import *

def main():
    while True:
        print_line(30)
        render_menu()
        option = int(input("\t ....Type the Option: "))
        print_line(30)
        if option == 1: 
            connection_data = get_data()
            mysql_connection(connection_data)
            break
        if option == 2: 
            connection_data = get_data()
            psql_connection(connection_data)
            break
        if option == 3:
            print("Leaving...")
            break
        if option == 4:
            connection_data = get_data()
            save_data(connection_data)
            break
        if option == 5:
            connection_data = fetch_data()
            if(connection_data['management-system'] == "MySQL"):
                mysql_connection(connection_data)
            else: 
                psql_connection(connection_data)
            break

def mysql_connection(connection_data):
    conn = connect_to_database(connection_data)           
    if(conn):
        execute_mysql_query(conn)

def psql_connection(connection_data):
    conn = connect_to_database(connection_data)           
    if(conn):
        execute_mysql_query(conn)

if __name__ == "__main__":
    main()