cantidad_combos = int(input())
Pa, Pb, Pc = input().split() # El split separa los valores ingresados por espacios
Pa = int(Pa)
Pb = int(Pb)
Pc = int(Pc)

for v in range(cantidad_combos):
    combo = input()
    total = combo.count('A') * Pa + combo.count('B') * Pb + combo.count('C') * Pc # Calcula el total del combo contando cuántas A, B y C hay en el combo e multiplicándolas por su respectivo daño
    print(total)