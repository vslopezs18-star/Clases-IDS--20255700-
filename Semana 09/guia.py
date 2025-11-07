usuarios = []
productos = []

cafeteria = True

while cafeteria:
    Menu_principal =  int(input("""1. Mostrar productos
                                2. Agregar productos
                                3.	Registrar nuevo cliente
                                4.	Mostrar clientes
                                5.	Registrar pedido
                                6.	Mostrar pedidos del día
                                7.	Mostrar categorías disponibles
                                8.	Salir"""))
    if Menu_principal == 1:
        