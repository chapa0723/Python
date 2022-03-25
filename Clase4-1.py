#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y #otro final.

def impares(inicio, fin):
    for i in range(inicio, fin):
        if i % 2 != 0:
            print(i)