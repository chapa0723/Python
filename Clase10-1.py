#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.
from cProfile import label
from msilib.schema import RadioButton
import tkinter as tk
from tkinter import ttk
windows = tk.Tk()

# (0,0) (1,0) (2,0)

# (0,1) (1,1) (2,1)

# (0,2) (1,2) (2,2) 

radioValue = tk.IntVar()
windows.columnconfigure(0, weight=1) # es para el label user_label

#limpiar radiobutton
limpiar = ttk.Button(windows, text="Limpiar", command=lambda: radioValue.set(0))
limpiar.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

#radio boton
radioboton =ttk.Radiobutton(windows, text="Radioboton 1", variable=radioValue, value=1)
radioboton.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

radioboton2 =ttk.Radiobutton(windows, text="Radioboton 2", variable=radioValue, value=2)
radioboton2.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

radioboton3 =ttk.Radiobutton(windows, text="Radioboton 3", variable=radioValue, value=3)
radioboton3.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

radioboton4 =ttk.Radiobutton(windows, text="Radioboton 4", variable=radioValue, value=4)
radioboton4.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)





windows.mainloop()
