# Vamos a jugar un juego

aprobacion = True
while aprobacion:
    eleccion = input("¿Quieres seguir jugando? (Y/N)")
    if eleccion[0].lower() == "n": # La variable que indica que sigamos jugando o no es aprobacion, pones el lower para que no importe si es mayúscula o no
        aprobacion = False # Ahora aprobacion es false
    elif eleccion[0].lower() == "y": # Aquí tanto en la primera como en la segunda pones el [0] porque si pone yes o no solo evaulará la primera letra no importando si es mayúscula o no
        print("Me alegra que quieras seguir jugando!")
    else:
        print("La opción elegida no es válida.")