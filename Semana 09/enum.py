usuarios = ["Ana", "Carlo", "Luis", "Maria"]

for posicion, usuario in enumerate(usuarios,start=1): # Enumerate hace una secuencia de números según la cantidad de valores que tenga el iterable, básicamente los enumera en uno, dos y tres. Le ponemos que inicie en 1. Enumerate solo permite un iterable
    print(f"{posicion} {usuario}")