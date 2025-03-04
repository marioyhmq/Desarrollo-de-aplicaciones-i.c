from src.models import Gerente, JefeArea, Asistente, Tecnico


def crear_empleados():
    gerente = Gerente("Carlos", "Ramírez")

    jefes = [
        JefeArea("María", "López", "Marketing", gerente),
        JefeArea("Jorge", "Fernández", "Sistemas", gerente),
        JefeArea("Ana", "González", "Producción", gerente),
        JefeArea("Luis", "Torres", "Logística", gerente)
    ]

    for jefe in jefes:
        gerente.agregar_jefe_area(jefe)

    empleados = []
    for jefe in jefes:
        for i in range(2):
            empleado = Asistente(f"Asistente{i+1}", jefe.area, jefe)
            empleados.append(empleado)
            jefe.agregar_subordinado(empleado)
        
        for i in range(3):
            empleado = Tecnico(f"Tecnico{i+1}", jefe.area, i+1, jefe)
            empleados.append(empleado)
            jefe.agregar_subordinado(empleado)

    return gerente, jefes, empleados
