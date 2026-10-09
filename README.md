CRUD Parametrizado
Decisiones tomadas:

¿Se borra de verdad?
DELETE real · marcar activo = 0

¿Qué pasa con los hijos?
Cascada · impedir el borrado · dejarlos huérfanos

¿Quién asigna el ID?
La base (autoincremento) · el programa

Seguridad
Todas las consultas SQL se realizan mediante parámetros para evitar inyección SQL.