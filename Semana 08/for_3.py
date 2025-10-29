personas = ["Ana", "Luis", "Luisa"]

for p in personas: # Todo este es para que ponga cada letra en una línea
    for l in p:
        print(l) 

valores = [[1, 3, 6], 
           [2, 7, 4], 
           [6, 5, 9], 
           [1, 10, 20]]

mayores = [] # Le ponemos así porque será una lista
minimo = int(input("Digite el mínimo: "))

for v in valores:# Este es para que se vaya a la lista en general
    for valorcito in v: # Este es para que se vaya a cada una de las listas dentro de la lista
        if valorcito > 6:
         mayores.append(valorcito) # Aquí se le va a agregando a la lista mayores los que son mayores a 6 de la lista valores
        
print(mayores)