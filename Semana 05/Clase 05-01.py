# Clase repaso

nombre = "Valeria"
palabra = "RECONOCER"
palabra2 = "ratón"

print(nombre[2:5:1]) # El último indica cada cuánto hará los saltos
print(palabra[1::2])
print(palabra2[::-1]) # Ese - indica que va a empezar de final al inicio

##############################

prueba = "carretón"

print(prueba==prueba[::-1]) #Esto es para verificar si es un palíndromo o no, o sea que si se lee igual de derecha a izquierda como de izquierda a derecha

# Los números si los ponemos así tal cual sin comillas no tienen len, solo el texto cuando se ponen las comillas

edad = input(26) # Lo que es un input es un string a pesar de que sea un número, si yo quiero que se comporte como un número le tengo que poner int antes del input

