import pandas as pd
from models import Asistente, Gerente, JefeDeArea, PersonalTecnico

def crear_empleados():
    gerente = Gerente("Carlos Pérez")
    jefe_marketing = JefeDeArea("Ana Gómez", "Marketing", gerente.nombre)
    jefe_sistemas = JefeDeArea("Juan Ruiz", "Sistemas", gerente.nombre)
    asistente1 = Asistente("Pedro López", jefe_marketing.nombre)
    asistente2 = Asistente("Luis Fernández", jefe_sistemas.nombre)
    tecnico1 = PersonalTecnico("Sofía Díaz", 3, jefe_marketing.nombre)
    tecnico2 = PersonalTecnico("Martín Chávez", 5, jefe_sistemas.nombre)
    
    jefe_marketing.agregar_asistente(asistente1)
    jefe_marketing.agregar_tecnico(tecnico1)
    jefe_sistemas.agregar_asistente(asistente2)
    jefe_sistemas.agregar_tecnico(tecnico2)
    
    return [gerente, jefe_marketing, jefe_sistemas, asistente1, asistente2, tecnico1, tecnico2]

def formatear_datos(empleados):
    data = [{"Nombre": e.nombre, "Puesto": e.puesto, "Experiencia": e.experiencia or "N/A", "Jefe": e.get_jefe_inmediato(), "Estado": e.get_estado()} for e in empleados]
    return pd.DataFrame(data)