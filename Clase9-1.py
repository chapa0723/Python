#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

listado = str(input("Introduce una lista de países: "))
listado = listado.split()
liastado = listado.sort()
print (listado)
listado = set(listado)
print(", ".join(listado))


#brasil chile peru argentina peru chile peru brasil