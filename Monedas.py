#convertidor de monedas
cantidad = float(input("cantidad en MXN: "))
print("Monedas: 1. usd 2. eur 3. thb 4. jpy 5. krw 6. aud 7. pen 8. cad 9. ves 10. ars")
opcion =int(input(" elige opcion: "))
match opcion:
    case 1:
        resultado = cantidad / 16.5
        unidad = "USD"
    case 2:
        resultado = cantidad / 18.0
        unidad = "EUR"
    case 3:
        resultado = cantidad / 0.45
        unidad = "THB"
    case 4:
        resultado = cantidad / 0.12
        unidad = "JPY"
    case 5:
        resultado = cantidad / 0.013
        unidad = "KRW"
    case 6:
        resultado = cantidad / 11.5
        unidad = "AUD"
    case 7:
        resultado = cantidad / 2.8
        unidad = "PEN"
    case 8:
        resultado = cantidad / 0.2
        unidad = "CAD"
    case 9:
        resultado = cantidad / 0.0023
        unidad = "VES"
    case 10:
        resultado = cantidad / 0.046
        unidad = "ARS"
    case _:
        print("Opción inválida. Por favor, ingrese un número del 1 al 10.")
        resultado = None

if resultado is not None:
    print("convertido:", resultado, unidad)