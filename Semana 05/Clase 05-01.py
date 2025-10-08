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

edad = int(input()) # Lo que es un input es un string a pesar de que sea un número, si yo quiero que se comporte como un número le tengo que poner int antes del input
# print(len(edad)) # Aquí lo va a tomar como string o sea texto porque sigue siendo texto el 26 al solo dejar input

print(palabra.lower()) # El lower es un método, que hace que se haga minúscula
print(palabra2.upper()) # Aquí será mayúscula
print(palabra2.capitalize()) # Llevan paréntesis porque como los métodos son funciones aplicables a un objeto tienen que llevar paréntesis

# La capitalize es para que la primera letra sea mayúscula