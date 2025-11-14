# Empiezo con crear la función para registrar los préstamos

def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    """Registra los préstamos que se vayan haciendo"""
    carnet = input("Ingrese su carnet: ")
    # Verifico que el carnet este registrado en la lista de estudiantes, para eso me voy al diccionario en la clave carnet de la lista de estudiantes
    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante["carnet"] == carnet:
            encontrado = True
            print("El carnet sí está registrado")
    # Aquí hago saber que el carnet ingresado no existe y vuelve al inicio
    if encontrado == False:
        print("Este carnet no está registrado")
        return
    
    código = input("Ingrese el código del libro: ")
    # Hago un diccionario vacío para almacenar los códigos de los libros a prestar       
    libro_actual = {}
    for libro in lista_libros:
        if libro["código"] == código:
                libro_actual = libro
    # Si no hay libros con el código ingresado entonces muestro un mensaje, pero si sí entonces aviso que se encontró 
    if len(libro_actual) == 0:
        print("El código ingresado no pertenece a ningún libro")
        return
    else:
        print("El libro fue encontrado")
    # Veo si el estado del libro para mostrar si está prestado o no    
    if libro_actual["disponible"] == False:
        print("El libro actualmente está prestado")
        return
    
        
    fecha = input("Ingrese la fecha del préstamo (ej. DD/MM/AAAA): ")
    # Hago un diccionario para que todos los datos ingresados se vayan a la lista de los préstamos
    préstamo = {
        "carnet del estudiante": carnet,
        "código del libro": código,
        "fecha": fecha
    }
    lista_prestamos.append(préstamo)
    # Aquí pongo el libro como ya no disponible
    libro_actual["disponible"] = False
    print("El préstamo fue registrado con éxito.")
    
# Ahora hago la función para mostrar los préstamos que se hacen

def mostrar_prestamos(lista_prestamos):
    """Muestra los préstamos realizados"""
    # Verifico si hay préstamos o no
    if len(lista_prestamos) == 0:
        print("No hay préstamos actualmente.")
        return
    else:
        print(lista_prestamos)