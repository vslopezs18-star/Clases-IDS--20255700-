uno = float(input())
dos = float(input())
tres = float(input())
cuatro = float(input())
cinco = float(input())
seis = float(input())

lista = [uno , dos, tres, cuatro, cinco, seis]

print(f"Maximo: {max(lista):.2f}")
print(f"Minimo: {min(lista):.2f}")
print(f"Diferencia: {(max(lista) - min(lista)):.2f}") # Acordate de la sintaxis de las cosas, el orden y si no hay operaciones que hagan directamente lo que queres como el promedio entonces con las operaciones que ya hiciste las haces, solo es lógica Vale vos podes
print(f"Suma: {sum(lista):.2f}")
print(f"Promedio: {(sum(lista) / len(lista)):.2f}")