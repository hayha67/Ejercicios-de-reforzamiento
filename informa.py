#brindar informacion
consulta = input("Ingrese nombre de artista, pelicula o series: ").lower()
match consulta:
    case "inception":
        info = "Inception es una película de ciencia ficción dirigida por Christopher Nolan"
    case "beatles":
        info = "The Beatles fue una banda de rock británica formada en Liverpool en 1960"
    case "stranger things":
        info = "Stranger Things es una serie de televisión de ciencia ficción y terror"
    case _:
        info = "No se encontró información"
print("informacion:", info)