M = int(input())
S = int(input())
A = str(input())
B = str(input())

texto_con_saltos = A[::S]
texto_final = texto_con_saltos + "_Alvin" + (B * M)
print(texto_final)