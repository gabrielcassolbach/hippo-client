import json
from colorama import init, Fore, Back, Style
from tabulate import tabulate

def render_menu():
    print_line(30)
    print("Welcome to HIPPO-CLIENT \n ---- Options: ")
    print("\t -- 1 to enter in MySql Server \t")
    print("\t -- 2 to enter in Postgree Server \t")
    print("\t -- 3 to quit \t")
    print_line(30)

def render_logo():
    print(Fore.CYAN + "")
    logo1()

def print_line(size):
    for i in range(1, int(size)):
        print("--", end="")
    print("")

def get_data():
    connection_dict = {}
    connection_dict['host'] = input("type your host: ")
    connection_dict['user'] = input("type your user: ")
    connection_dict['port'] = input("type your port: ")
    connection_dict['password'] = input("type your password: ")
    connection_dict['database'] = input("type your database name: ")
    choice = int(input("type 1 to save data or 0 otherwise: "))
    if(choice == 1):
        save_data(connection_dict)
    return connection_dict

def render_options_menu():
    print_line(30)
    print("---- Options: ")
    print("\t 1 to see database tree \t")
    print("\t 2 to run a query \t")
    print_line(30)
    
def fetch_data():
    try:
        with open('connection_data.json', 'r') as file:
            data = json.load(file)
            return data 
    except FileNotFoundError:
        print("File not Found")
    except json.JSONDecodeError:
        print("Json error")    

def save_data(connection_data):
    with open('connection_data.json', 'w') as file:
        json.dump(connection_data, file, indent=4)
    print("connection data stored")

def logo1():
    hippo = """
        HIPPO CLIENT

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
