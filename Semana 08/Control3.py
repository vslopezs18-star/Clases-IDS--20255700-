platosypedidos = True

agente = "encargado"
platillo = []
precios = []

nombre_ingresado = ""

while nombre_ingresado.lower() != agente.lower():
        nombre_ingresado = input("Favor ingrese el nombre del agente: ")
        if nombre_ingresado.lower() != agente.lower():
            print("Agente no registrado")
            print(f"{nombre_ingresado}")
            
while platosypedidos:
    opción = int(input("1. Creación de platillos, 2.Consulta de platillos y precios, 3.Colocar un pedido, 4. Salir"))
    if opción == 1:
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))
    elif opción == 2:
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados.")
        else:
            for v in range(len(platillo)):
                print(f"{platillo[v].capitalize()}: ${precios[v]:.2f}")
    elif opción == 3:
        platillo_elegido = input("Indique el nombre del platillo para su orden: ")
        if platillo_elegido.lower() in platillo:
            indice = platillo.index(platillo_elegido.lower())
            print(f"Usted ha elegido {platillo[indice]} con un precio de {precios[indice]}")
        elif platillo_elegido.lower() not in platillo:
            print("Ese platillo no existe")
    elif opción == 4:
            platosypedidos = False
    