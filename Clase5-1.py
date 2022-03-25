#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def triangulo(altura,base):
    area = (altura*base)/2
    return area

def circulo(radio):
    area = 3.1416*radio**2
    return area