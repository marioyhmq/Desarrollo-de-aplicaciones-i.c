class Empleado:
    def __init__(self, nombre, puesto, experiencia=None, jefe_inmediato=None, estado='TC'):
        self.nombre = nombre
        self.puesto = puesto
        self.experiencia = experiencia
        self.jefe_inmediato = jefe_inmediato
        self.estado = estado

    def get_resumen(self):
        resumen = f"{self.nombre} - {self.puesto}"
        if self.experiencia:
            resumen += f" | {self.experiencia} años de experiencia"
        return resumen

    def get_jefe_inmediato(self):
        return self.jefe_inmediato if self.jefe_inmediato else "No tiene jefe inmediato"

    def get_estado(self):
        estados = {'TC': 'Término de Contrato', 'D': 'Despido', 'R': 'Renuncia'}
        return estados.get(self.estado, 'Desconocido')

class Gerente(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Gerente")
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class JefeDeArea(Empleado):
    def __init__(self, nombre, area, jefe_inmediato):
        super().__init__(nombre, "Jefe de Área", jefe_inmediato=jefe_inmediato)
        self.area = area
        self.asistentes = []
        self.tecnicos = []

    def agregar_asistente(self, asistente):
        if len(self.asistentes) < 2:
            self.asistentes.append(asistente)
        else:
            print("No se pueden agregar más de dos asistentes")

    def agregar_tecnico(self, tecnico):
        if len(self.tecnicos) < 5:
            self.tecnicos.append(tecnico)
        else:
            print("No se pueden agregar más de cinco técnicos")

class PersonalTecnico(Empleado):
    def __init__(self, nombre, experiencia, jefe_inmediato):
        super().__init__(nombre, "Técnico", experiencia=experiencia, jefe_inmediato=jefe_inmediato)

class Asistente(Empleado):
    def __init__(self, nombre, jefe_inmediato):
        super().__init__(nombre, "Asistente", jefe_inmediato=jefe_inmediato)