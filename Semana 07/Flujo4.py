# El for repite algo cierta cantidad de veces hasta que haya una condición que me diga que pare
# Iterable quiere decir que tengo varios elementos para recorrer, ejemplos son una lista, una cadena de texto, un rango de números, etc.
# Iterable es capaz de devolver sus componentes uno a la vez
# Iterador es un objeto que representa un flujo de datos, es decir, un objeto que puede ser recorrido elemento por elemento

nombres = [1, 2, 3, 0] # Aquí tengo un iterable (lista) y tres iteradores (1, 2, 3)

for numerito in nombres: # El for crea un iterador que recorre el iterable nombres, el numerito no necesita ser declarado antes porque el for lo crea automáticamente
    print("Hola") # Imprime cada uno de los elementos del iterable nombres
    print(numerito) # Imprime cada uno de los elementos del iterable nombres
    
print(len(nombres[0])) # Esto me da error porque el entero no es un iterable, no puedo recorrerlo