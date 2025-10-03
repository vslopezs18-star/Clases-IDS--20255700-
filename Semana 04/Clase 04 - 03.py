"""ItemIngresar = input("Ingrese el item: ")
print(f"El item ingresado es {ItemIngresar}")  """ #Strings son las palabras y conjuntos de texto, cadena de caracteres, se puede validar por True/False como los otros tipos de datos

# El + hace un espacio para que salga con espacio y no todo junto
# La función len es el largo (es un blank, espacio vacío)

"""s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))"""

# Ese es el ejemplo de cuando pones len y te va a poner los espacios
# La cadena de caracteres es Python las interpreta como arreglos []

my_string = "ABCDEFCCC" # string o cadena de carecteres

"""letra = int(input("Indique el indice de la letra a mostrar")) # Aquí me va a adar error en la terminal porque cada vez que se pone input lo agarra como texto, entonces para arreglarlo se pone int antes de input
print(my_string[letra])
3
print(len(my_string)) # Ejemplo NO DE INT
print(my_string[0])"""

# Los índices comienzan desde 0, o sea el primer elemento de una secuencia tiene índice 0, el segundo 1 y así
# Para acceder a un elemento, utilizamos corchetes después del nombre de la secuencia y dentro de los corchetes colocamos el índice del elemento que queremos obtener

# Slices (subsettings)

print(my_string[1:5:3]) # Los dos puntos es como decir "desde, hasta", pero el último elemento que pono en este caso 4 no será ese el último porque es exclusivo, entonces llegará hasta el tercero
# El segundo dos puntos es para indicar los saltos, si le pondo dos es porque se va a saltar uno sí uno no
# Índices negativos son los que empiezan desde el final de la secuencia, -1 hace referencia al útlimo elemento, -2 el penúltimoy así

print("H" is my_string)
print("O" not in my_string)

print("AJP" *8) # Aquí hago una repetición
print(min(my_string)) # min siginifica el menor
print(max(my_string)) # max es el mayor
print(my_string.count("C")) # aquí cuenta cuantas veces aparece el elemento que le pongo

# El punto es para poner operaciones dentro del texto que se puede, como encontrar la mayúsucula y más cosas, en este caso se llama método porque a la string le aplico una "función" que se llama en realidad método