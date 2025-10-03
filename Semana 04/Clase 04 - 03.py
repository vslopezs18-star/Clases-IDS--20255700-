# ItemIngresar = input("Ingrese el item: ")
# print(f"El item ingresado es {ItemIngresar}")  Strings son las palabras y conjuntos de texto, cadena de caracteres, se puede validar por True/False como los otros tipos de datos

# El + hace un espacio para que salga con espacio y no todo junto
# La función len es el largo (es un blank, espacio vacío)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

# Ese es el ejemplo de cuando pones len y te va a poner los espacios
# La cadena de caracteres es Python las interpreta como arreglos []

my_string = "ABCDE" # string o cadena de carecteres
letra = int(input("Indique el indice de la letra a mostrar")) # Aquí me va a adar error en la terminal porque cada vez que se pone input lo agarra como texto, entonces para arreglarlo se pone int antes de input
print(my_string[letra])
3
print(len(my_string)) # Ejemplo NO DE INT

# Los índices comienzan desde 0, o sea el primer elemento de una secuencia tiene índice 0, el segundo 1 y así
# Para acceder a un elemento, utilizamos corchetes después del nombre de la secuencia y dentro de los corchetes colocamos el índice del elemento que queremos obtener

print(my_string[0])
