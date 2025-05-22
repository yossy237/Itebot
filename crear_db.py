import sqlite3

conn = sqlite3.connect("itebot.db")
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS menus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ayudas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comando TEXT NOT NULL,
    descripcion TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS palabras_clave (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palabra TEXT UNIQUE NOT NULL,
    respuesta TEXT NOT NULL
)
''')

# Insertar datos iniciales (usando INSERT OR IGNORE para evitar duplicados)
cursor.execute("INSERT OR IGNORE INTO palabras_clave (palabra, respuesta) VALUES (?, ?)", 
               ("hola", "¡Hola! ¿En qué puedo ayudarte?"))

cursor.execute("INSERT OR IGNORE INTO palabras_clave (palabra, respuesta) VALUES (?, ?)", 
               ("ayuda", "Puedes escribir 'menu' para ver las opciones disponibles."))

cursor.execute("INSERT OR IGNORE INTO menus (nombre, descripcion) VALUES (?, ?)", 
               ("principal", "Menú principal con opciones."))

cursor.execute("INSERT OR IGNORE INTO ayudas (comando, descripcion) VALUES (?, ?)", 
               ("comando1", "Este es un ejemplo de ayuda para comando1."))

conn.commit()
conn.close()

print("Base de datos creada con éxito y datos iniciales insertados.")