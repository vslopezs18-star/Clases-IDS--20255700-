# Sistema de gestion de alumnos

menu_iniciado = True
alumnos = []

while menu_iniciado: 
    opción = int(input("1.Agregar, 2.Consular, 3.Modificar, 4. Borrar, 5. Salir"))
    if opción == 5:
      menu_iniciado = False
    elif opción == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
        print(alumnos)
    elif opción == 2:
      for a in alumnos: # Este es cuando suponemos que ya tenemos una lista completa vamos a decir que para cada a en alumnos va a ser primero uno, luego dos y así
          print(a)
    elif opción == 3:
        indice = int(input("Digite el numero del alumno (1-3): "))
        nuevo = input("Digite el nombre nuevo: ")
        alumnos[indice-1] = nuevo
    elif opción == 4:
        indice = int(input("Digite el número del alumno (1-3) a popear: "))
        alumno_borrado = alumnos.pop(indice-1) # Aquí estamos guardando al que borramos
        print(f"Hemos borrado a : {alumno_borrado}")
    else:
        print("Esa opción no es válida.")
print("Gracias por usar nuestro sistema.")