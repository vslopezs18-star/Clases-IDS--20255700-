# Primero creo la función para registrar estudiantes

def registrar_estudiante(lista_estudiantes):
    """Registra el nombre y carnet de los estudiantes"""
    nombre = input("Nombre: ".capitalize())
    # Como se tienen que crear automáticamente los carnets pongo las condiciones para cada caso
    numeros = len(lista_estudiantes) + 1
    if numeros < 10:
        carnet = "S00" + str(numeros)
    elif numeros < 100:
        carnet = "S0" + str(numeros)
    else:
        carnet = "S" + str(numeros)
    # Guardo todos los datos en un diccionario para que se agreguen a la lista de estudiantes
    estudiante = {
        "carnet": carnet,
        "nombre": nombre.capitalize()
    }
    
    lista_estudiantes.append(estudiante)
    # De igual manera pongo un mensaje para que se sepa el carnet correspondiente al estudiante
    print(f"Estudiante registrado: {nombre.capitalize()} con carnet {carnet}.")

# Luego creo la función para mostrar los estudiantes

def mostrar_estudiantes(lista_estudiantes):
    """Muestra a los estudiantes registrados"""
    # Si no hay estudiantes entonces pongo un mensaje para que lo diga y regrese al inicio
    if len(lista_estudiantes) == 0:
        print("No hay ningún estudiante registrado aún")
        return
    else:
        print(lista_estudiantes)