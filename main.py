from connect import *


def main():
    server = input("mysql os psql")

    conn2 = connect_to_database_psql()

    #conn = connect_to_database()
    #if conn:
    #    while True:
    #        query = input("Digite sua consulta SQL(sair para encerrar o programa): ")
    #        if query.lower() == 'sair':
    #            break
    #        query_database(conn, query)
    #   close_connection(conn)


if __name__ == "__main__":
    main()

# criar as conexões com os servidores. (bibliotecas)

# primeiramente -> mysql.

# biblioteca "gráfica" => puxar os dados do servidor e filtrar 

# pela nossa biblioteca. 

# 