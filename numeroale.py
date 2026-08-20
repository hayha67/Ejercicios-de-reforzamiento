#adivinar numero
import random
secreto = random.randint(1, 100)
while True:
    intento = int(input("Adivina el número secreto (entre 1 y 100): "))
    if intento < secreto:
        print("demasiado bajo")
    elif intento > secreto:
        print("demasiado alto")
    else:
        print("¡Felicidades! Adivinaste el número secreto:", secreto)
        break