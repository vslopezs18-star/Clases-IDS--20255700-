usuario = "Alvin"


# Validar el usario 
usuario == "Javier"

# Mostrar menus segun usario 

# Definir tareas para usuario

# Presentar resumenes del ususario

cantidad_alumunos = 74
media_edad = 18.231234
monto_hope = 1234567.8901
inversion_evento = -98765.21548

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
print(f"con edad promedio de {media_edad: .2f} años") # Después de la variable le pones dos puntos y el formato que queres, en este caso fue que quería dos decimales en vez del montón
print(f"colectaron {monto_hope:,.2f} como un donativo") # La coma antes del . indica que lo quiero ver en miles entonces dice 1,234.57 o sea la forma cambio más no el fondo
print(f"y la totalida de gastos fue de ${abs(inversion_evento):,.2f} dolares") #El abs manda el valor absoluto del número, el $ se lo pones antes para que salga como dólares

print(type(usuario) is str)

esta_lloviendo = False #Esta es una situación, entonces cuando le des type será bool de booleano
print(type(esta_lloviendo) is bool) #Lo podes comprobar poniendo is o is not
print(type(monto_hope) is not bool)

#No puedo sumar palabras, entonces se contatena 

nombre = "Vale"
apellido = "López"
nombre_completo = nombre + " " + apellido
print(nombre_completo)