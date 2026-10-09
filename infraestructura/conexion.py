import sqlite3


def obtener_conexion():

    conexion = sqlite3.connect("datos/empresa.db")

    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion