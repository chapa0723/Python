#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

class vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

coche = vehiculo("Ford", "Fiesta", "Rojo")

f = open("vehiculo.txt", "w")
f.write(str(coche.marca) + " " + str(coche.modelo) + " " + str(coche.color))
f.close()
f = open("vehiculo.txt", "r")
print(f.read())
f.close()

