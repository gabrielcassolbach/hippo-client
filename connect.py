import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
#import psycopg2

#def connect_to_database_psql():
#    try:
#        conn = psycopg2.connect(
#            host="localhost",
 #
 #
 #
 #          password="postgres",
  #          database="template1",
   #         port="5433"
    #    )
     #   #if conn.is_connected():
        #    print("Conexão bem-sucedida")
        #    return conn
    #except psycopg2.DatabaseError as err:
     #   print(f"Erro: {err}")
      #  return None



def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="University"
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar: {err}")
        return None

def execute_query():
    query = query_text.get("1.0", tk.END).strip()
    if not query:
        messagebox.showwarning("Aviso", "A consulta SQL está vazia.")
        return

    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            display_results(results)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao executar a consulta: {err}")
        finally:
            cursor.close()
            conn.close()

def display_results(results):
    for row in results_tree.get_children():
        results_tree.delete(row)
    for row in results:
        results_tree.insert("", tk.END, values=row)

# Configuração da janela principal
root = tk.Tk()
root.title("Cliente de Banco de Dados")

# Configuração do frame principal
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Caixa de texto para a consulta SQL
query_label = ttk.Label(mainframe, text="Consulta SQL:")
query_label.grid(row=0, column=0, sticky=tk.W)

query_text = tk.Text(mainframe, height=10, width=70)
query_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Botão para executar a consulta
execute_button = ttk.Button(mainframe, text="Executar", command=execute_query)
execute_button.grid(row=2, column=1, sticky=tk.E)

# Árvore para exibir os resultados
results_tree = ttk.Treeview(mainframe, columns=(1, 2, 3), show='headings')
results_tree.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

for col in results_tree["columns"]:
    results_tree.heading(col, text=f"Coluna {col}")

# Configuração das margens e preenchimento
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()


