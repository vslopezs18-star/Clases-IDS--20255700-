tuplaplatos = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
tuplacomplemento = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

plato_principal = int(input())
complemento = int(input())

print(f"El pedido de Alvin es: {tuplaplatos[plato_principal-1]} con {tuplacomplemento[complemento-1]}")