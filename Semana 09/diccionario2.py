# Los diccionarios son mutables
birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}
birthdays["Carol"] = "Sep 12"

print(birthdays["Carol"]) # En los diccionarios no se trabaja con índices sino con CLAVES

birthdays["Pau"] = "Julio 31" # También se pueden agregar items
print(birthdays)

del birthdays["Bob"] # Con del borras en los diccionarios
print(birthdays)

# Keys son las claves y value los valores de cada clave. La combinación de todo son los items
# Los keys, values y items son secuencias que entonces son iterables para los que se puede ocupar for

for v in birthdays.values():
    print(v)
    
for i in birthdays.keys():
    print(i)
    
for persona, date in birthdays.items():
    print(f"El cumpleaños de {persona} es el día {date}.")