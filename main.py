from connect import *
from graphic_engine import *

def main():
    while True:
        render_logo()
        render_menu()
        option = int(input("\t ....Type the Option: "))
        print_line(30)
        if option == 1:
            option = int(input("use stored connection: 1 else 0: "))
            if(not option):
                connection_data = get_data()
            else: 
                connection_data = fetch_data()
            mysql_connection(connection_data)
            break
        if option == 2: 
            option = int(input("use stored connection: 1 else 0: "))
            if(not option):
                connection_data = get_data()
            else: 
                connection_data = fetch_data()
            psql_connection(connection_data)
            break
        if option == 3:
            print("Leaving...")
            break
                
def mysql_connection(connection_data):
    conn = connect_to_database(connection_data)           
    render_options_menu()
    while True:
        options = int(input("select option: "))
        if(options == 1):
            tree_new(conn)
            break
        if(options == 2):
            execute_mysql_query(conn)
            break

def psql_connection(connection_data):
    conn = connect_to_database(connection_data)           
    if(conn):
        execute_mysql_query(conn)

if __name__ == "__main__":
    main()