from connect import *
import tkinter as tk
from tkinter import ttk, messagebox

def janela():

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
