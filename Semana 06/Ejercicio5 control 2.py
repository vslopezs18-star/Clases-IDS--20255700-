M = int(input())
S = int(input())
A = str(input())
B = str(input())

texto_con_saltos = A[::S] # Si pongo dos veces dos puntos y un número, significa que me corta la cadena y haré saltos del número que yo ponga ahí
texto_final = texto_con_saltos + "_Alvin" + (B * M)
print(texto_final)