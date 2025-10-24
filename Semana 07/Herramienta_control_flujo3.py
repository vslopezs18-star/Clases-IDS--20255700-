monto = float(input("Digite el monto: "))
tipo = input("Ingrese el tipo (Local/Export):   ")
impuesto = 0 # Inicializamos la variable impuesto, para evitar errores si no se cumple ninguna condición

if tipo.lower() == "local": # Este es para local 
    if monto > 500:
       print(f"El monto a pagar es: {monto * 0.10:.2f}") # Se puede hacer así o con una variable impuesto que va cambiando, en este caso es 10% entonces de un solo lo multiplicas
    else: 
        if monto > 200:
            print(f"El monto a pagar es: {monto * 0.08:.2f}")
        else: 
            if monto > 50:
                print(f"El monto a pagar es: {monto * 0.06:.2f}")
            else:
                impuesto = 0
                
if tipo.lower() != "local": # Este es para cuando no es local, o sea puede ser export, internacional, etc.
    if monto > 500:
       print(f"El monto a pagar es: {monto * 0.14:.2f}")
    else: 
        if monto > 200:
            print(f"El monto a pagar es: {monto * 0.12:.2f}")
        else: 
            if monto > 50:
                print(f"El monto a pagar es: {monto * 0.1:.2f}")
            else:
                print(f"El monto a pagar es: {monto * 0:.2f}")
                
elif tipo.lower() == "export": # Este es para export, que es diferente a local. Es cualquier otra cosa pero que se cumpla algo específico
    if monto > 500:
       print(f"El monto a pagar es: {monto * 0.14:.2f}")
    else: 
        if monto > 200:
            print(f"El monto a pagar es: {monto * 0.12:.2f}")
        else: 
            if monto > 50:
                print(f"El monto a pagar es: {monto * 0.1:.2f}")
            else:
                print(f"El monto a pagar es: {monto * 0:.2f}")
# else:
    # print("Ese tipo no es válido") # Si no es ni local ni export, entonces no es válido
    
# print(f"El impuesto a pagar de tipo {tipo} por venta de {monto:,.2f}") Este es por si no quiero ir poniendo print en cada condición, sino que al final ya lo imprima todo junto
# print(f"es de {monto*impuesto:,.2f}") Este para que muestre el impuesto total a pagar por último así como el anterior