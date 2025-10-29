inicio = 0
maximo = 5

while inicio < maximo: # Esta es el área de condición, mientras sea verdadera se ejecutará siempre pero hasta que ya no sea true o verdadera, este parará
    print("Saludo")
    inicio = inicio + 2
    
presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input("Digite el valor de compra: "))
    gasto += compra

gasto -= compra # El valor resultante del gasto va a ser antes del valor de la compra que me hizo pasar de mi presupuesto, entonces antes del con el que me pasé me da lo que sí pude gastar sin haberme pasado de 1000
print(gasto)

estado = "Conectado" 
while estado == "Conectado": # Mientras que sea conectado lo va a seguir haciendo
    print("Hola Sebas")
    estado = input("Digite su estado: ")