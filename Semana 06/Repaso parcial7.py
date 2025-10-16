nombre_competidor = str(input())
apellido = str(input())

nick = nombre_competidor[:5] + apellido[0]
pin = (len(nombre_competidor) * 1000 + len(apellido)) % 10000

print(f"Nick: {nick.lower()}")
print(f"Pin: {pin}")
print(f"ID: C3-{nick.lower()}-{pin}")