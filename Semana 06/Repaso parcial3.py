x = int(input())
a = input()
b = input()

primera_parte = len(a) / x
segunda_parte = len(b) / x

c = a[:int(primera_parte)] + b[-int(segunda_parte):] # Este orden de int es muy importante porque con él es que le decis a Python desde donde y cómo cortar
print(c)