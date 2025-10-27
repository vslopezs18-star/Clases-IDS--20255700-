cantidad_personas = int(input())
personas = 0 # contador de personas mayores o iguales a 15 años, siempre los contadores los pones fuera del bucle sino no funcionan

for v in range(cantidad_personas):
    edad = int(input())
   
    if edad >= 15:
        personas = personas + 1 # se suma 1 al contador si la persona es mayor o igual a 15 años

print(personas) # imprime el total de personas mayores o iguales a 15 años
