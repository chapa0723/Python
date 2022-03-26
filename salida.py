#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
import datetime
def salir():
    tiempo_actual = datetime.datetime.now()
    hora = tiempo_actual.hour
    if hora > 7:
        print("No es hora de salir")
    else:
        print("Es hora de salir")


        