from datetime import date

from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio


repo = EmpleadoRepositorio()

ana = Empleado(
    "12345678-9",
    "Ana Rojas",
    date(2024, 3, 1),
    950000
)

print("CREATE")
repo.guardar(ana)

print("READ")
print(repo.obtener("12345678-9"))

print("LIST")
print(repo.listar())

print("UPDATE")
ana.sueldo_base = 1050000
repo.actualizar(ana)
print(repo.obtener("12345678-9"))

print("DELETE")
print(repo.eliminar("12345678-9"))

print(repo.obtener("12345678-9"))