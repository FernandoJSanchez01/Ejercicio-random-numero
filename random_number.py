#Adivina el numero
import random as rn
x = "y"
while x == 'y':
    num = int(input("Digite un numero entra 1 y 10: "))
    value = rn.randint(1, 10)
    def aleatorio(value):
        if num == value:
            print(f"Adivinaste el numero es: {value}")
        elif num > 10:
            raise Exception("Sorry, el numero no puede pasar 10")
        else:
            print("El numero es incorrecto")
        return value
    aleatorio(value)
    x = input("Desea intentar nuevamente? (y/n) ")

