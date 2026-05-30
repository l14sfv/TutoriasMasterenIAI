# comandos de SQL

## creacion de la BD
sqlite3 mydb.db

#creacion de las tablas
CREATE TABLE usuarios {
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    edad INTEGER,
    activo BOOLEAN DEFAULT 0
}

import sqlite3
import bcrypt
import secrets
from datetime import datetime
from typing import List, Dict, Tuple

def contrasena_automatica(longitud: int = 8) -> str:
    return secrets.token_urlsafe(longitud)

def hash_contrasena(contrasena: str, salt: str = None) -> Tuple[str, str]:
    
    if salt is None:
        salt = bcrypt.gensalt().decode('utf-8')
        
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')
    return contrasena_hash, salt


#comandos
#conectar la BD o crearla si no existe
conn = sqlite3.connect('mydb.db')

#crear cursor para ejecutar comandos
a = conn.cursor()

#alguna consulta
a.execute("SELECT * FROM usuarios WHERE id = 1")

#obtener resultados
resultados = a.fetchall()

#insertar datos
a.execute("INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)", ("Juan Perez", "juan.perez@example.com", 30))

#Actualizar datos
a.execute("UPDATE usuarios SET id = 1 WHERE id = 1")

#Eliminar datos
a.execute("DELETE FROM usuarios WHERE id = 2")

#Ver las tablas creadas
.tables

#ver los schemas
.schemas productos

#guardar cambios
conn.commit()

#cerrar conexion
conn.close()

#metodos o funciones
# cursor() # crear un cursor para ejecutar comandos, da un objeto
# execute() # ejecutar una consulta SQL, recibe la consulta y los parametros
# executemany() # ejecutar una consulta SQL con multiples parametros, recibe la consulta y una lista de tuplas con los parametros
# fetchall() # obtener todos los resultados de una consulta, devuelve una lista de tuplas
# fetchone() # obtener un resultado de una consulta, devuelve una tupla o None si no hay mas resultados
# fetchmany(size) # obtener un numero de resultados de una consulta, devuelve una lista de tuplas
# commit() # guardar los cambios realizados en la BD
# close() # cerrar la conexion a la BD

# #atributos
# rowcount # numero de filas tocadas por la ultima consulta
# lastrowid # id del ultimo registro insertado
# description # descripcion de las columnas del resultado de una consulta
# rowfactory # metodo para personalizar el formato de los resultados

#tensor

#0D Escalar
#1D Vector
#2D Matriz
#3D Tensor

#pytorch
import numpy as np
import torch

a = torch.tensor(5) # 0D
b = torch.tensor([1, 2, 3]) # 1D
c = torch.tensor([[1, 2], [3, 4]]) # 2D
d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # 3D

#tensores aleatorios
e = torch.rand(3, 3) # 3x3 matriz de numeros aleatorios entre 0 y 1
f = torch.randn(3, 3) # 3x3 matriz de numeros aleatorios con distribucion normal
g = torch.zeros(3, 3) # 3x3 matriz de ceros
h = torch.ones(3, 3) # 3x3 matriz de unos
i = torch.eye(3) # matriz identidad de 3x3

#desde un ndarray de numpy

j = np.array([[1, 2], [3, 4]])
k = torch.from_numpy(j) # tensor a partir de un ndarray de numpy

#tensorflow

import tensorflow as tf

#constantes
a = tf.constant(5) # 0D
b = tf.constant([1, 2, 3]) # 1D
c = tf.constant([[1, 2], [3, 4]]) # 2D
d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # 3D

#ZEROS
z = tf.zeros((3, 3)) # 3x3 matriz de ceros

#NUMPY
import numpy as np
a = np.array(5) # 0D
b = np.array([1, 2, 3]) # 1D
c = np.array([[1, 2], [3, 4]]) # 2D
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) # 3D

q = np.zeros((20, 3, 3)) # 3x3 matriz de ceros