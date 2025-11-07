usuarios = ["Ana", "Carlo", "Luis", "Maria", "Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas = ["mango", "fresa", "pera", "sandia", "piña"]

for posicion, usuario in enumerate(usuarios,start=1): # Enumerate hace una secuencia de números según la cantidad de valores que tenga el iterable, básicamente los enumera en uno, dos y tres. Le ponemos que inicie en 1. Enumerate solo permite un iterable
    print(f"{posicion} {usuario}")
    
for p, u in zip(usuarios, edades): # Aquí zipeo dos listas, o sea combino dos listas y para eso tengo que poner el iterador que quiero a la izquierda primero y luego el otro
    print(f"{p} {u}")

for usuario, edad, fruta in zip(usuarios, edades, frutas):
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}.")