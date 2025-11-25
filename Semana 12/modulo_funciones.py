# Modulo para describir la lógica de las funciones

# Importamos el módulo de la función
import modulo_datos as dat

def registrar_estudiante():
    """Función para validad y registrar estudiantes"""
   # Le pongo carnet_i para no confundirme con carnet en general
    carnet_i = input("Digite el numero de carnet: ")
    nombre_i = input("Digite el nombre: ")
    apellido_i = input("Digite el apellido: ")