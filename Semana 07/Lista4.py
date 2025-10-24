nombres = ["Ana", "Antonio", "Ana", "José"] # La lista es una colección pero cada elemento de la lista también es una colección de caracteres
print(len(nombres[0])) # Aquí se está pidiendo la longitud del primer elemento de la lista nombres, que es "Ana"
print(nombres.count("Ana")) # Aquí cuenta cuantas veces aparece "Ana" en la lista nombres
print(nombres.count("a")) # Aquí cuenta cuantas veces aparece la letra "a" en la lista nombres, pero no funciona porque cada elemento es una colección y no se puede contar así dentro de cada elemento
print(nombres[0].count("a")) # Aquí cuenta cuantas veces aparece la letra "a" en el primer elemento de la lista nombres
print(nombres[0].lower().count("a")) # Aquí convierte el primer elemento de la lista nombres a minúsculas y luego cuenta cuantas veces aparece la letra "a"

r_a = 0  # Aquí se crea una variable r_a para guardar el resultado de la suma de las veces que aparece la letra "a" en cada elemento de la lista nombres
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")   
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a) # Aquí se está sumando la cantidad de veces que aparece la letra "a" en cada elemento de la lista nombres y se guarda en la variable r_a, que al final se imprime