import tkinter as tk
from tkinter import ttk
from counter import Counter

root = tk.Tk()
root.title("Janela")
root.geometry("400x300")

counter = Counter()

# Funcao pra chamar o botao contador de cliques
def on_click():
    count = counter.increment()
    label_var.set(f"Cliques: {count}")

button = ttk.Button(root, text="Clique aqui!", command=on_click)
button.pack()

label_var = tk.StringVar(value="Cliques: 0")
label = ttk.Label(root, textvariable=label_var)
label.pack()

root.mainloop()


