mi_mascota = {
    "tipo":"perro",
    "nombre":"Phoenix",
    "edad": 4, 
    "personalidad":"cariñosa"}

print(type(mi_mascota)) # Un diccionario está constituidos por items que se contruyen por clave: el valor.
print(len(mi_mascota))
print(mi_mascota)

regys_mascota = {       # Al diccionario no le importa el orden en el que están solo el contenido, entonces las compara con base en eso
    "edad":4,
    "nombre" :"Phoenix",
    "personalidad":"cariñosa",
    "tipo": "perro"
}

son_iguales = mi_mascota == regys_mascota
print(son_iguales)