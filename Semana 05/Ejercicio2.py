lista_completaprecios = [3.52, 55.15 , 4.25, 60.25, 5.65, 3.15, 2.65, 70.75, 6.25, 2.55]

plato = int(input())
variable1 = plato - 1

nuevo_precio = float(input())
lista_completaprecios[variable1] = nuevo_precio

print(f"Los precios actualizados son: {lista_completaprecios}")

# Corchete siempre es posición