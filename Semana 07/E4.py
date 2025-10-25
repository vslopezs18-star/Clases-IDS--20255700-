numero = int(input())

cont7 = 0
cont5 = 0

for v in range(numero):
    lista = int(input())
    if numero == 7:
        cont7 = cont7 + 1
    elif numero == 5:
        cont5 = cont5 + 1

print(cont7 and cont5)