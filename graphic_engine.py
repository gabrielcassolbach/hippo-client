import json

def render_menu():
    print("\t type 1 to psql \t")
    print("\t type 2 to mysql \t")
    print("\t type 3 to leave \t")
    print("\t type 5 to use stored connection \t")

def get_data():
    connection_dict = {}
    connection_dict['management-system'] = "MySQL"
    connection_dict['host'] = input("type your host: ")
    connection_dict['user'] = input("type your user: ")
    connection_dict['port'] = input("type your port: ")
    connection_dict['password'] = input("type your password: ")
    connection_dict['database'] = input("type your database name: ")
    choice = int(input("type 1 to save data or 0 otherwise"))
    if(choice == 1):
        save_data(connection_dict)
    return connection_dict
    
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
