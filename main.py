from connect import *
from graphic_engine import *
from colorama import init, Fore, Back, Style

def main():
    while True:
        print_line(30)
        render_menu()
        option = int(input("\t ....Type the Option: "))
        print_line(30)

        if option == 100:
            print(Fore.CYAN + "")
            #print(Back.YELLOW + "Este texto tem fundo amarelo")
            #print(Style.BRIGHT + "Este texto é dim")
            logo1()
            print(Style.RESET_ALL + "Este texto volta ao normal")
        if option == 15:
            connection_data = get_data()
            conn = connect_to_database(connection_data)
            imprimir_hierarquia_mysql(conn)


        if option == 10:
            connection_data = get_data()

            conn = connect_to_database(connection_data) #Teste           

            info(conn, 'department')


        if option == 30:
            connection_data = get_data()

            conn = connect_to_database(connection_data) #Teste           

            export_to_csv(conn, 'department')




        if option == 40:
            connection_data = get_data()

            conn = connect_to_database(connection_data) #Teste           

            export_to_json(conn, 'department')




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