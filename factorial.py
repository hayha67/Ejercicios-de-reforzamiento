# factorial
factorial = int(input("Ingrese un número factorial: "))
num= 1
if num < 0:
     print("Error: No se puede calcular el factorial de un número negativo.")
else:
     for i in range(1,num+1):
          factorial*=i
print("El factorial de", num, "es:", factorial)