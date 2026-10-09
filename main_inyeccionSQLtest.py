from datetime import date

from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio


repo = EmpleadoRepositorio()

carlos = Empleado(
    "22222222-2",
    "Carlos Perez",
    date(2024, 5, 15),
    850000
)

print("CREATE")
repo.guardar(carlos)

print("READ")
print(repo.obtener("22222222-2"))

print("LIST")
print(repo.listar())

print("UPDATE")
carlos.sueldo_base = 950000
repo.actualizar(carlos)
print(repo.obtener("22222222-2"))

print("DELETE")
print(repo.eliminar("22222222-2"))

print(repo.obtener("22222222-2"))

print("\nPRUEBA DE INYECCION SQL")

print(
    repo.listar(
        nombre_contiene="' OR '1'='1"
    )
)

print(
    repo.obtener(
        "' OR '1'='1"
    )
)