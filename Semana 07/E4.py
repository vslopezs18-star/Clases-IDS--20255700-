numero = int(input())

cont7 = 0
cont5 = 0

for v in range(numero): # Repite el bloque de código 'numero' veces
    n = int(input())    # Lee un número entero y después con el if lo compara con 7 y 5 y cuenta cuántas veces aparecen, se le suma 1 al contador correspondiente porque empezaba en 0
    if n == 7:
        cont7 = cont7 + 1
    if n == 5:
        cont5 = cont5 + 1

print(cont7, cont5) # La coma separa los dos valores a imprimir