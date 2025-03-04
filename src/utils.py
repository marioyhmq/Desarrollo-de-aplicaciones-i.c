from models import Gerente, JefeArea, Asistente, Tecnico

def crear_empleados():
    # Creando un gerente
    gerente = Gerente("Carlos", "Ramírez")

    # Creando jefes de área
    jefes = [
        JefeArea("María", "López", "Marketing", gerente),
        JefeArea("Jorge", "Fernández", "Sistemas", gerente),
        JefeArea("Ana", "González", "Producción", gerente),
        JefeArea("Luis", "Torres", "Logística", gerente)
    ]

    for jefe in jefes:
        gerente.agregar_jefe_area(jefe)

    # Creando asistentes y técnicos
    empleados = []
    for jefe in jefes:
        for i in range(2):  # Máximo 2 asistentes por área
            empleado = Asistente(f"Asistente{i+1}", jefe.area, jefe)
            empleados.append(empleado)
            jefe.agregar_subordinado(empleado)
        
        for i in range(3):  # Máximo 5 técnicos por área
            empleado = Tecnico(f"Tecnico{i+1}", jefe.area, i+1, jefe)
            empleados.append(empleado)
            jefe.agregar_subordinado(empleado)

    return gerente, jefes, empleados
