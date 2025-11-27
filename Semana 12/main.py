# Este modulo contiene el menú, o sea el inicio del programa

# Importamos las funciones de módulo_funciones.py

import modulo_funciones as fn

def salir():
    """Función para salir del programa"""
    print("Gracias por utilizar nuestro sistema.")
    
while True:
    print("""
      --- Menu Principal ---
        1. Registrar estudiante
        2. Inscribir en curso
        3. Generar reportes
        4. Salir
      """
)
    opcion = input("Indique su opción [1-4]: ")
    
    if opcion == "1": # Acordate de ponerlo en comillas porque lo vas a evaluar como texto, no como número
        fn.registrar_estudiante() # Aquí le digo que de fn llame a la función, en vez de hacerlo arriba con from e import
    elif opcion == "2":
        fn.inscribir_en_curso()
    elif opcion == "3":
        fn.generar_reporte()
    elif opcion == "4":
        salir()
        break
    else:
        print("La opción elegida no es válida.")