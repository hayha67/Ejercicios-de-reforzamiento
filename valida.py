# calcula de nota final con validacion de rango
parcial = float(input(" Nota del parcial: "))
proyecto = float(input(" Nota del proyecto: "))
examen = float(input(" Nota del examen l: "))

if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
    print("Error: Las notas deben estar entre 0 y 100.")
else:
    nota_final = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print("La nota final es:", nota_final)