#vocales no vocales

while True:
    letra = input("Ingrese una letra: ")
    if letra =="":
        break
    letra = letra .lower()
if letra in "aeiou":
    print("La letra es una vocal.")
else:
    print("La letra no es una vocal.")