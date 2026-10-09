from datetime import date

from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio

repo = EmpleadoRepositorio()

print("===== CREATE =====")

juan = Empleado(
    "33333333-3",
    "Juan Soto",
    date(2024, 6, 10),
    800000
)

repo.guardar(juan)

print("Empleado creado correctamente")


print("\n===== READ EXISTENTE =====")

empleado = repo.obtener("33333333-3")

print(empleado)


print("\n===== READ INEXISTENTE =====")

print(repo.obtener("99999999-9"))

print("\n===== LISTAR TODOS =====")

empleados = repo.listar()

for e in empleados:
    print(e)


print("\n===== FILTRO POR NOMBRE =====")

resultado = repo.listar("Juan")

for e in resultado:
    print(e)


print("\n===== FILTRO SIN RESULTADOS =====")

resultado = repo.listar("ZZZZZZ")

print(resultado)


print("\n===== UPDATE =====")

juan.sueldo_base = 1200000

filas = repo.actualizar(juan)

print("Filas actualizadas:", filas)

print(repo.obtener("33333333-3"))


print("\n===== UPDATE INEXISTENTE =====")

fantasma = Empleado(
    "44444444-4",
    "Fantasma",
    date(2024, 1, 1),
    100000
)

print(repo.actualizar(fantasma))


print("\n===== DELETE EXISTENTE =====")

print(repo.eliminar("33333333-3"))


print("\n===== VERIFICAR BORRADO =====")

print(repo.obtener("33333333-3"))


print("\n===== DELETE INEXISTENTE =====")

print(repo.eliminar("99999999-9"))


print("\n===== INYECCION SQL LISTAR =====")

resultado = repo.listar(
    nombre_contiene="' OR '1'='1"
)

print(resultado)


print("\n===== INYECCION SQL OBTENER =====")

print(
    repo.obtener(
        "' OR '1'='1"
    )
)