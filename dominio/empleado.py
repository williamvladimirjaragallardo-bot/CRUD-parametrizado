class Empleado:

    def __init__(self, rut, nombre, fecha_ingreso, sueldo_base):
        self.rut = rut
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.sueldo_base = sueldo_base

    def __str__(self):
        return (
            f"Empleado("
            f"rut={self.rut}, "
            f"nombre={self.nombre}, "
            f"fecha_ingreso={self.fecha_ingreso}, "
            f"sueldo_base={self.sueldo_base})"
        )