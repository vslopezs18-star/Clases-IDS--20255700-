numeros = [1, 2, 3, 4]

# print(len(numeros))
palabra = "Aulas" # Aulas también es una colección
print(len(palabra))

for v in palabra:
    print("Hola")
    
dias = ["Lunes", "Martes", "Miércoles", 
        "Jueves", "Viernes", "Sábado", "Domingo"]

for d in dias[2]: # Recorre cada letra del tercer elemento de la lista 'dias', que es "Miércoles"
    print(d) # Imprime cada letra de "Miércoles" en una línea diferente
    
for p in dias:
    print(p[:2]) # Imprime las dos primeras letras de cada elemento de la lista 'dias'

print(range(1,10)) # Imprime el objeto range que va del 1 al 9, el último es el que no se incluye, range es una lista que genera los valores en el momentoen que se necesita

for i in range(0,10,2):
    print(i) # Imprime los números del 0 al 9 de 2 en 2