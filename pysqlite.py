import sqlite3
import re


# Conexión y creación de tabla
conn = sqlite3.connect("alumnos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    correo TEXT
)
""")
conn.commit()

# Función para validar correo electrónico
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(patron, correo) is not None

# Función para agregar estudiante
def agregar_estudiante(nombre, edad, correo):
    if not validar_correo(correo):
        print("Correo electrónico inválido.")
        return

    try:
        cursor.execute("INSERT INTO estudiantes (nombre, edad, correo) VALUES (?, ?, ?)",
                       (nombre, edad, correo))
        conn.commit()
        print("Estudiante agregado.")
    except sqlite3.Error as e:
        print(f"Error al agregar estudiante: {e}")

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

# Función para buscar estudiante por nombre
def buscar_por_nombre(nombre):
    cursor.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(fila)
    else:
        print("No se encontró ningún estudiante con ese nombre.")

# Menú principal
while True:
    print("\n1. Agregar estudiante\n2. Mostrar todos\n3. Buscar por nombre\n4. Salir")
    op = input("Elige una opcion: ")

    if op == '1':
        nombre = input("Nombre: ")
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad inválida.")
            continue
        correo = input("Correo: ")
        agregar_estudiante(nombre, edad, correo)
    elif op == '2':
        mostrar_estudiantes()
    elif op == '3':
        nombre = input("Nombre a buscar: ")
        buscar_por_nombre(nombre)
    elif op == '4':
        break
    else:
        print("Opcion no válida.")

# Cierre de conexión
conn.close()

