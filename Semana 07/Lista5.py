nombres = ["Ana", "Antonio", "Paulina", "José"] # Si yo le pido un len a nombres me va a devolver la cantidad de elementos que hay en la lista, o sea 4
print(nombres) # Ahora se imprime la lista completa
nombres[2] = "Pablo"
print(nombres) # Ahora el tercer elemento de la lista nombres es "Pablo"

nombres.append("Hazel") # Agrega "Hazel" al final de la lista nombres
print(nombres) # Ahora se imprime la lista completa con el nuevo elemento

nombres.append(input("Ingrese el nuevo nombre: ")) # Pide al usuario que ingrese un nombre y lo agrega al final de la lista nombres
print(nombres) # Ahora se imprime la lista completa con el nuevo elemento ingresado por el usuario

nombres.insert(3,"Sebas") # Inserta "Sebas" en la posición 3 de la lista nombres
print(nombres) # Ahora se imprime la lista completa con el nuevo elemento en la posición 3

nombres.insert(int(input("Indique el índice: ")), "Sebas") # Pide al usuario que ingrese un índice y agrega "Sebas" en esa posición de la lista nombres
print(nombres) # Ahora se imprime la lista completa con el nuevo elemento en la posición indicada por el usuario

nombres.insert(int(input("Indique el índice: ")), input("Nombre: ")) # Pide al usuario que ingrese un índice y un nombre, y agrega el nombre en esa posición de la lista nombres
print(nombres) # Ahora se imprime la lista completa con el nuevo elemento en la posición indicada

nombres.remove("Sebas")
print(nombres) # Ahora se imprime la lista completa sin el elemento "Sebas"

nombre_borrado = nombres.pop(int(input("Índice a borrar: "))-1) # Pide al usuario que ingrese un índice, elimina el elemento en esa posición de la lista nombres y lo guarda en la variable nombre_borrado
print(nombres)
print(nombre_borrado)

# Pop no aplica en colección de strings directamente, ya que strings son inmutables. Sino que por recorrido.