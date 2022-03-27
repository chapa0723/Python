import tkinter as tk
from tkinter import ttk
windows = tk.Tk()

# (0,0) (1,0) (2,0)

# (0,1) (1,1) (2,1)

# (0,2) (1,2) (2,2) 

radioValue = tk.IntVar()
windows.columnconfigure(0, weight=1) # es para el label user_label
#windows.columnconfigure(1, weight=3)


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

#Boton
loginboton=ttk.Button(windows, text="Login")
loginboton.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)







windows.mainloop()