#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(self.nombre, self.nota)
    def aprobado(self):
        if self.nota >= 7:
            print("Aprobado")
        else:
            print("Reprobado")

a = Alumno("Juan", 8)
a.imprimir()
a.aprobado()