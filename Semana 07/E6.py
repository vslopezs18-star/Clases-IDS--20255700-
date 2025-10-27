N_nombres = int(input())

for v in range(N_nombres): # Repite el bloque de código 'N_nombres' veces
    nombre = input() # Aquí se lee el nombre ingresado, va uno por uno entonces no tenes que poner un input varias veces porque se repite cada vez. O sea, si pones 3 en N_nombres, se va a repetir 3 veces el input para que ingreses 3 nombres diferentes.
    cantidad_letras = len(nombre) # len() cuenta la cantidad de letras que tiene el nombre ingresado.
    
    if cantidad_letras <= 6:
        print("No vale la pena")
        
    if cantidad_letras >= 8:
        print("Si aguanto otro desarrollo de personaje") 
        
    if 6 < cantidad_letras < 8:
        print("Dios no creo aguantar esta vez")