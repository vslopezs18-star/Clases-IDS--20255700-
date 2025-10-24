nombres = ["Ana", "Sebas", "Mario", "Carla"] # Aquí tengo un iterable (lista) y cuatro iteradores (Ana, Sebas, Mario, Carla)
#Encontremos a Sebas

for n in nombres:
    if n == "Sebas": # Si el iterador n es igual a "Sebas"
        print("Ya lo encontré") # Imprime "Ya lo encontré"
    else: 
        print("Aquí no está")