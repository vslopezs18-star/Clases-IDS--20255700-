cantidad_combos = int(input())

Pa = int(input())
Pb = int(input())
Pc = int(input())

for v in range(cantidad_combos):
    combos = input()
    daño_total = 0
    
    for e in range(6): # 
        boton = combos
        
        if boton == 'A':
            daño_total = daño_total + Pa
        if boton == "B":
                daño_total = daño_total + Pb
        if boton == "C":
                daño_total = daño_total + Pc
                
    print(daño_total)