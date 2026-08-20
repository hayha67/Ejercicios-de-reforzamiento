# programa para calcular salario neto de un empleado
salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
porcentaje = float(input("Ingrese el impuesto (%): "))
deducciones = float(input("Ingrese las deducciones: "))
impuesto = salario_bruto * (porcentaje / 100)
salario_neto = salario_bruto - impuesto - deducciones
print("El salario neto del empleado es:", salario_neto)