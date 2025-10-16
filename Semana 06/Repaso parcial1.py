correo = input()
  
unarroba = correo.count("@")==1 
unpunto = correo.count(".") >=1
espacios = correo.count(" ")==0
puntoinicial = correo[0]!="."
puntofinal = correo[-1]!="."
caracteres = correo.index("@")
antes = correo[:caracteres]
despues = correo[caracteres+1:]
validar = len(antes) >=3  and len(despues) >=3

print(unarroba and unpunto and puntofinal and puntoinicial and espacios and validar)