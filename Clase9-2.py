#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

import functools
def impares(lista):
    listado = filter(lambda x: x % 2 != 0, lista)
    #return filter(lambda x: x % 2 != 0, lista)
    suma = functools.reduce(lambda x, y: x + y, listado)
    print (suma)
    
impares ([1,2,3,4,5,6,7,8,9,10])


