import pandas as pd
import tkinter as tk
from tkinter import messagebox

def alterExcel(route):
    print('Ola mundo')
    newRoute = route.replace('"','')
    df = pd.read_excel(newRoute, header=None)

    for x in range(0, len(df)):
        phoneNumber = df.loc[x][0]
        alterNumber = phoneNumber.replace('(','').replace(')','').replace('-','').replace(' ','')
        finalNumber = "55" + alterNumber
        df.iloc[x][0] = finalNumber
        
    print(df)
    df.to_excel("contatos_atualizado.xlsx", index=False)
    
def on_button_click():
    road = entry.get()
    messagebox.showinfo("Resultado", f"Lista atualizado com sucesso")
    alterExcel(road)

# Criando a janela principal
root = tk.Tk()
root.title("Atualizar contatos no Excel")

# Criando um rótulo (label)
label = tk.Label(root, text="Cole o caminho da pasta Excel:")
label.pack(pady=10)

# Criando uma caixa de entrada (entry)
entry = tk.Entry(root)
entry.pack(pady=10)

# Criando um botão
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=10)
# Iniciando o loop principal da interface

root.mainloop()


