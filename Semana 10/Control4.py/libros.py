# Creo la función para registrar los libros que se vayan agregando

def registrar_libro(lista_libros):
    """Registra cada libro que se agrega"""
    título = input("Título: ")
    autor = input("Autor: ")
    # Aquí genero el código de los libros automáticamente según sea el caso
    numero = len(lista_libros) + 1
    if numero < 10:
        código = "L00" + str(numero)
    elif numero < 100:
        código = "L0" + str(numero)
    else:
        código = "L" + str(numero)
    # Almaceno todos los datos en un diccionario para que se agreguen a la lista de libros
    libro = {"código": código,
                 "título": título,
                 "autor": autor,
                 "disponible": True
                 }
    lista_libros.append(libro)

# Creo la función para mostrar los libros que se van regsitrando

def mostrar_libros(lista_libros):
    """Muestra los libros registrados"""
    # En el caso que no hayan libros registrados, mostraré un mensaje que lo diga y regresará al inicio
    if len(lista_libros) == 0:
        print("No hay libros registrados aún")
        return
    # Corroboro los estados de los libros para ver su estado y mostrarlos
    for libro in lista_libros:
        if libro["disponible"]:
            estado = "Disponible"
        else:
            estado = "Prestado"
        # Muestro los datos de cada libro registrado
        print(f"Código: {libro["código"]}")
        print(f"Título: {libro["título"]}")
        print(f"Autor: {libro["autor"]}")
        print(f"Estado: {estado}")



