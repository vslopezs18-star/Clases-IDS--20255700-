numero = int(input())

if 2 <= numero <= 1000:
    if numero % 2 == 0:
        print(numero + 2)   
        print(numero - 1)
    else: 
        print(numero + 1)
        print(numero - 2)