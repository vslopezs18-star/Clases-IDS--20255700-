# Empiezo con crear la función para registrar los préstamos

def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    """Registra los préstamos que se vayan haciendo"""
    carnet = input("Ingrese su carnet: ")
    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["carnet"] == carnet:
            encontrado = True
            print("El carnet sí está registrado")
    
    if encontrado == False:
        print("Este carnet no está registrado")
        return
    
    código = input("Ingrese el código del libro: ")
           
    libro_actual = {}
    for libro in lista_libros:
        if libro["código"] == código:
                libro_actual = libro
        
    if len(libro_actual) == 0:
        print("El código ingresado no pertenece a ningún libro")
        return
    else:
        print("El libro fue encontrado")
        
    if libro_actual["disponible"] == False:
        print("El libro actualmente está prestado")
        return
    
        
    fecha = input("Ingrese la fecha del préstamo (ej. DD/MM/AAAA): ")
    
    préstamo = {
        "carnet del estudiante": carnet,
        "código del libro": código,
        "fecha": fecha
    }
    lista_prestamos.append(préstamo)
    
    libro_actual["disponible"] = False
    print("El préstamo fue registrado con éxito.")
    
# Ahora hago la función para mostrar los préstamos que se hacen

def mostrar_prestamos(lista_prestamos):
    """Muestra los préstamos realizados"""
    if len(lista_prestamos) == 0:
        print("No hay préstamos actualmente.")
        return
    else:
        print(lista_prestamos)