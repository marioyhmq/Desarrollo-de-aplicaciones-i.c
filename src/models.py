class Empleado:
    def __init__(self, nombre, apellido, puesto, jefe=None, estado="Activo"):
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.jefe = jefe
        self.estado = estado

    def get_resumen(self):
        return f"{self.puesto} - {self.nombre} {self.apellido}"

    def get_jefe_inmediato(self):
        return self.jefe.get_resumen() if self.jefe else "No tiene jefe"

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class Tecnico(Empleado):
    def __init__(self, nombre, apellido, años_experiencia, jefe, estado="Activo"):
        super().__init__(nombre, apellido, "Técnico", jefe, estado)
        self.años_experiencia = años_experiencia

    def get_resumen(self):
        return f"{super().get_resumen()} - {self.años_experiencia} años de experiencia"

class Asistente(Empleado):
    def __init__(self, nombre, apellido, jefe, estado="Activo"):
        super().__init__(nombre, apellido, "Asistente", jefe, estado)

class JefeArea(Empleado):
    def __init__(self, nombre, apellido, area, gerente, estado="Activo"):
        super().__init__(nombre, apellido, f"Jefe de {area}", gerente, estado)
        self.area = area
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Gerente(Empleado):
    def __init__(self, nombre, apellido, estado="Activo"):
        super().__init__(nombre, apellido, "Gerente", None, estado)
        self.jefes_area = []

    def agregar_jefe_area(self, jefe):
        self.jefes_area.append(jefe)
