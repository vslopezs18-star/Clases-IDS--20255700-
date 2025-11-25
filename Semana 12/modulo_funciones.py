# Modulo para describir la lógica de las funciones

# Importamos el módulo de la función
import modulo_datos as dat

def registrar_estudiante():
    """Función para validad y registrar estudiantes"""
   # Le pongo carnet_i para no confundirme con carnet en general
    while True:
        carnet_i = input("Digite el numero de carnet: ")
        caraceter_carnet = len(carnet_i)
        valido = True # Por defecto tiene que ser primero True, a menos que cuando haga la búsqueda uno por uno y encuentra que no existe entonces es False
        
        for a in dat.alumnos: 
            if a["carnet"] == carnet_i:
                valido = False
        if caraceter_carnet >= 6 and caraceter_carnet <= 10 and valido:
            break
        else:
            print("El número de dígitos debe ser entre 6 y 10.")
            
    while True:    
        nombre_i = input("Digite el nombre: ")
        if len(nombre_i) >= 2:
            break
        else:
            print("El número de caracteres del nombre debe ser al menos 2")
    while True:
        apellido_i = input("Digite el apellido: ")
        if len(apellido_i) >= 2:
            break
        else:
            print("El número de caracteres del nombre debe ser al menos 2")
    alumno = {"carnet": carnet_i, 
              "nombre": nombre_i, 
              "apellido": apellido_i}
    
    dat.alumnos.append(alumno) # Aquí de modulo de datos estoy llendome a alumno que es una lista y le digo que agregue alumno, o sea los diccionarios que se vayan creando

    