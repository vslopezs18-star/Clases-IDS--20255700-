alumnos = ["Juan", "Ana", "Pedro"]

orden = int(input("Orden en el que entraste(1-3): "))

print(f"El niño que entró en orden {orden} se llama {alumnos[orden-1]}") # Ese orden-1 es para que no agarre 1 como 0 entonces así es fácil
