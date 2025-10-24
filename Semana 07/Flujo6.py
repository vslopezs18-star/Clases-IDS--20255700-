nombres = ["Ana", "Sebas", "Mario", "Carla"]
nombre_buscar = input("Nombre a buscar:")

for n in nombres:
    if n == nombre_buscar: # Si el iterador n es igual a nombre_buscar
        print("Ya lo encontré") # Imprime "Ya lo encontré"
    else: 
        print("Aquí no está")