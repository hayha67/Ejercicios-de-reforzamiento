#contador de numeros impares
N = int(input("Ingrese un número entero positivo: "))
i = 1
while True:
    if i % 2 !=0:
        print(i, end=" ")
    i += 1
    if i > N:
        break
print("\n" " finalizado el conteo de números impares hasta", N)