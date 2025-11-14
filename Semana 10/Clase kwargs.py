def regisrtro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesor, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")
        
regisrtro_profesores(
    "Alvin", 
    "Portillo",
    Ciclo1 = ["BD1", "IIJ", "A&GD"],
    Ciclo2 = ["DAI", "BD2", "SINE"],
    Ciclo3 = ["IDS", "FPEN", "PAD"]
)