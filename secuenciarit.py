#secuencia aritemtica
inicio = int(input("primer numero: "))
diferencia = int(input("diferencia: "))
limite = int(input("Limite: "))
num= inicio
while True:
    print(num, end=" ")
    num += diferencia
    if num > limite:
        break
print("\n" "secuencia aritmetica desde", inicio, "hasta", limite,)