# Modulo para describir la lógica de las funciones

# Importamos el módulo de la función
import modulo_datos as dat

def registrar_estudiante():
    """Función para validar y registrar estudiantes"""
   # Le pongo carnet_i para no confundirme con carnet en general
   
    while True:
        try:
            carnet_i = input("Digite el numero de carnet: ")
            
            if not carnet_i:
                raise ValueError("El carnet no puede estar vacío.")
            
            if not 6 <= len(carnet_i) <= 10:
                raise ValueError("El carnet debe tener entre 6 y 10 caracteres.")
            
            for alumno in dat.alumnos:
                if alumno["carnet"] == carnet_i:
                    raise ValueError("Este carnet ya existe.")
            break
        
        except ValueError as e:
            print(f"{e}")
            
    while True:    
        try:
            nombre_i = input("Digite el nombre: ") 
            
            if len(nombre_i) < 2:
                raise ValueError("El nombre debe de tener mínimo 2 caracteres.")
            break
        
        except ValueError as v:
            print(f"{v}")
            
            
    while True:
        try:
            apellido_i = input("Digite el apellido: ")
            if len(apellido_i) < 2:
                raise ValueError("El número de caracteres del apellido debe ser al menos 2")
            break
        
        except ValueError as f:
            print(f"{f}")
            
    alumno = {"carnet": carnet_i, 
              "nombre": nombre_i, 
              "apellido": apellido_i}
    
    dat.alumnos.append(alumno) # Aquí de modulo de datos estoy llendome a alumno que es una lista y le digo que agregue alumno, o sea los diccionarios que se vayan creando

def inscribir_en_curso():
    """Función para guardar las inscripciones"""
    
    carnet_valido = ""
    while True:
    
        try:
            carnet_i = input("Digite su carnet o salir para regresar al menú: ")
        
            if carnet_i.lower() == "salir":
             return
        
            existe = False
            for alumno in dat.alumnos:
                if alumno["carnet"] == carnet_i:
                 existe = True
                 break
            
            if not existe:
                raise ValueError("El carnet ingresado no existe.")
        
            carnet_valido = carnet_i
            break
    
        except ValueError as c:
            print(f"{c}")
    
    while True:
        
        try:
            for codigo, nombre in dat.cursos.items():
                print(f"[{codigo}] [{nombre}]")
                
            curso_i = input("Ingrese el codigo del curso o salir para regresar: ").upper()
            
            if curso_i.lower() == "salir":
             return
         
            if curso_i not in dat.cursos:
                raise KeyError("No existe el código que ingresó.")
        
            if (carnet_valido, curso_i) in dat.inscripciones:
                raise ValueError(f"El estudiante ya está inscrito en {curso_i}.")
        
            nueva_inscripcion = (carnet_valido, curso_i)
            dat.inscripciones.append(nueva_inscripcion)
        
        except KeyError as k:
            print(f"{k}")
        except ValueError as v:
            print(f"{v}")
    
def generar_reporte():
    """Muestra todo lo realizado"""
    
    if not dat.inscripciones:
        print("No hay inscripciones.")
        return
                
    while True:
        
        try:
            print("Seleccione un curso o 'SIN' para los estudiantes no inscritos: ")
            for codigo in dat.cursos:
                print(f"\t{codigo}")
            print("\tSIN Estudiantes sin inscripcion")
            print("\tX (Por si desea salir del submenú)")
            
            opcion = input("Opción: ").upper()
            
            if opcion == "X":
                break
            
            if opcion == "SIN":
                carnets_iunicos = []
                
                for carnet_i, _ in dat.inscripciones:
                    if carnet_i not in carnets_iunicos:
                        carnets_iunicos.append(carnet_i)
                
                encontrados = False
                for alumno in dat.alumnos:
                    if alumno["carnet"] not in carnets_iunicos:
                        print(f"{alumno["nombre"]} {alumno["apellido"]} {alumno["carnet"]}")
                        encontrados = True
                        
                if not encontrados:
                    print("Todos los alumnos tienen ingresado al menos un curso.")
            
            elif opcion in dat.cursos:
                print(f"Estudiantes en {dat.cursos[opcion]}")
                count = 0
                
                for inscripcion in dat.inscripciones:
                    if inscripcion[1] == opcion:
                        print(f"Carnet: {inscripcion[0]}")
                        count += 1
                
                if count == 0:
                    print(f"No hay estudiantes inscritos en {dat.cursos[opcion]}")
                    
            else:
                raise ValueError("Opción no válida.")
        
        except ValueError as r:
            print(f"{r}")
            
                
            
                
        
                
    