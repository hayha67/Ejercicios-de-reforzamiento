#convertidor de temperatura
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print("1. farenheit \n2. kelvin")
opcion = int(input("Ingrese la opción de conversión (1 o 2): "))
match opcion:
    case 1:
        resultado = (celsius * 9/5) + 32
        Unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        Unidad = "K"
    case _:
        resultado = None
        print("Opción inválida. Por favor, ingrese 1 o 2.")
if resultado is not None:
    print("convertido:", resultado, Unidad)