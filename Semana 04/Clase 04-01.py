usuario = "Alvin"


# Validar el usario 
usuario == "Javier"

# Mostrar menus segun usario 

# Definir tareas para usuario

# Presentar resumenes del ususario

cantidad_alumunos = 74
media_edad = 18.231234
monto_hope = 1234.56

print(type(cantidad_alumunos))
print(type(media_edad))

print(type(cantidad_alumunos)is int) # no es lo mismo "int" o sea no le pongas comillas, porque sino quiere decir que es literalmente int y no queres eso
print(type(media_edad)is int)

print("el usuario es" , "Alvin" , "y tiene" , "74" , "pajaritos en su aula")
print("el usario es", usuario , "y tiene" , cantidad_alumunos , "pajaritos en su aula") # Podes ponerle simplemente usuario y entiende porque ya puse la variable usuario como Alvin, al igual que con la edad y lo demás
print("y la edad promedio es de" , media_edad)

# F string es un texto formateado, para hacerlo solo se pone una f antes del texto
# Los corchetes abren la posibilidad de hacer cálculos o devolver los valores de las variables

print(f"El usario es {usuario}")
print(f"y en su aula con {cantidad_alumunos - 4} pajaritos en su aula")
print(f"con edad promedio de {media_edad: .2f} años") # después de la variable le pones dos puntos y el formato que queres, en este caso fue que quería dos decimales en vez del montón