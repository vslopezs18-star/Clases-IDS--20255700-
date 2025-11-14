# Este módulo contendrá las funciones

# Definiendo la función

def ordenar_pizza(size, masa, *ingredientes): # Ahora con args sirve para listas en cambio kargs sirve para diccionarios
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t - {i}")
        