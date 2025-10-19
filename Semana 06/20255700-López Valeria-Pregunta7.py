dui = input()

largo = len(dui)==10
noveno = dui[8]=="-"
ultimo = type(int(dui[-1])) is int

validar = largo and noveno and ultimo
print(validar)