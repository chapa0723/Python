#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter as tk
from tkinter import StringVar, ttk



windows = tk.Tk()

#User name
username_label = ttk.Label(windows, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5) # la W indica que se va a colocar a la izquierda segun el eje cartesiano en ingles (WEST)
username_entry = ttk.Entry(windows)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

#Password
pass_label = ttk.Label(windows, text="Password:")
pass_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
pass_entry = ttk.Entry(windows, show="*") #show="*" indica que se muestre el password con asteriscos
pass_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

#despegable/seleccionable
lista = ttk.Combobox(windows)
lista.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

#listado de opciones
opciones = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
lista["values"] = opciones

#lista para el listbox
listado = ["Adidas", "Nike", "Puma", "Hummel", "Reebok", "Asics"]
listado_item = StringVar(value=listado) #Convierto la lista en una variable de tipo StringVar que soporta tkinter

#listbox
listbox = tk.Listbox(windows, height=20, listvariable=listado_item)
listbox.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)






windows.mainloop()

