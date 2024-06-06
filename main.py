import os
from connect import *
from graphic_engine import *

def main():
    while True:
        os.system("clear")
        render_logo()
        render_menu()
        option = input("\t ---- Select your option: ")
        print_line(30)
        os.system("clear")
        match option: 
            case "1":
                mysql_connection(stored_connection_loop())
                if(not return_to_menu()):
                    break   
            case "2": 
                psql_connection(stored_connection_loop())
                if(not return_to_menu()):
                    break
            case "3":
                print("Leaving...")
                break
            case _:
                print(Fore.RED + "invalid input...")
                print(Fore.CYAN)

def return_to_menu():
    while True:
        option = (input(" Do you want to return to menu: \n yes or no: "))
        match option:
            case "no": 
                return 0
            case "yes":
                return 1
            case _:
                print(Fore.RED + "invalid input...")
                print(Fore.CYAN)

def stored_connection_loop():
    while True:
        option = (input(" Do you want to use a store connection? \n yes or no: "))
        match option:
            case "no": 
                return get_data()  
            case "yes":
                return fetch_data()
            case _:
                print(Fore.RED + "invalid input...")
                print(Fore.CYAN)

def mysql_connection(connection_data):
    os.system("clear")
    conn = connect_to_database(connection_data)           
    render_options_menu()
    while True:
        options = input("Select option: ")
        match options: 
            case "1":
                tree_new(conn)
                break
            case "2":
                execute_mysql_query(conn)
                break
            case _:
                print(Fore.RED + "wrong option...")
                print(Fore.CYAN)
    
def psql_connection(connection_data):
    conn = connect_to_database_psql(connection_data)           
    if(conn):
        execute_mysql_query(conn)

if __name__ == "__main__":
    main()