#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

conn = sqlite3.connect('sqlite3/misalumnos.db') #abre el archivo de base de datos
cursor = conn.cursor() # genera un cursor para realizar consultas en la base de datos

inserta = cursor.execute("INSERT INTO Alumnos VALUES (1,'Ramiro','Ramirez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (2,'Gonzalo','Gonzalez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (3,'Rodrigo','Rodriguez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (4,'Juan','Perez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (5,'Javier','Gomez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (6,'Juan','Lopez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (7,'Juan','Gonzalez')")
inserta = cursor.execute("INSERT INTO Alumnos VALUES (8,'Juan','Garcia')")

rows = cursor.execute('SELECT * FROM Alumnos') # ejecuta la consulta
consulta = cursor.execute ('SELECT * FROM alumnos WHERE nombre = "Rodrigo"') # ejecuta la consulta que busca el registro con el campo "nombre" = "Rodrigo"
for row in rows:
    print (row)
print ("\n Consulta:", consulta)

cursor.close()
conn.close()