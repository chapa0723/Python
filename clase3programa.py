def masaCorporal () : 
    peso = int (input("Ingrese su peso: "))
    altura = float (input("Ingrese su altura: "))
    imc = peso / (altura * altura)
    print ("Su indice de masa corporal es: ")
    print (round(imc,2))
masaCorporal()
