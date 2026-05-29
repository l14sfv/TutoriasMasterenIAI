# import numpy as np

# // vector 1 (vector 1)
# v = np.array([1, 2, 3])

# // matriz 2 ( vector 2)
# m = np.array([4,5,6],[7,8,9])

# print(v)
# print(m)

# print(v.shape) # (3,) - 3 elementos en una dimension
# print(m.shape) # (2,3) - 2 filas y 3 columnas

# print(v.ndim) # 1 - vector unidimensional
# print(m.ndim) # 2 - matriz bidimensional

#inversa A,X,Y

#resolver AX = Y

#A [1,2,3,4], Y = [5,6]

import numpy as np

# A = np.array([[1., 2.], [3., 4.]])
# Y = np.array([5., 6.])

# #inversa de A
# A_inv = np.linalg.inv(A)    # A^-1
# X = A_inv @ Y               # X = A^-1 Y

# print("A_inv = \n", A_inv)
# print("X = \n", X)

# Xa = np.linalg.solve(A, Y) # resolver AX = Y directamente
# print("Xa = \n", Xa)

# Y_calculada = A @ X # verificar que A @ X = Y
# print("Y_calculada = \n", Y_calculada)

# #producto matricial
# # A @ Y = 
# h = np.dot(A, Y) # o A @ B 
# print("h = \n", h)

# #transpuesta
# # A_T = A.T # o 
# j = np.transpose(Y)
# print("j = \n", j)

# #sqtr = np.sqrt(16) # raiz cuadrada
# # exp = np.exp(1) # e^1
# # log = np.log(10) # logaritmo natural de 10
# # sin = np.sin(np.pi/2) # seno de pi/2

# # algebra lineal
# np.linalg.norm(X) # norma de un vector
# np.linalg.det(A) # determinante de una matriz
# np.linalg.eig(A) # valores y vectores propios de A
# np.linalg.inv(A) # inversa de A
# np.linalg.solve(A, Y) # resolver AX = Y
# np.linalg.svd(A) # descomposición en valores singulares de A

# # aleatorias
# z = np.random.rand(2,2) # vector de 3 números aleatorios entre 0 y 1 - decimales
# print("z = \n", z)

# q = np.random.randint(1, 10, size=(2,3)) # matriz de 2 filas y 3 columnas con enteros aleatorios entre 1 y 9
# print("q = \n", q)

# #decimales mayores a 1
# y = 0 + 30 * np.random.rand(2,2) # matriz de 2 filas y 2 columnas con números aleatorios entre -5 y 5
# print("y = \n", y)

# #pesos de modelo
# e = np.random.randn(3,3) # matriz de 3 filas y 3 columnas con números aleatorios de una distribución normal
# print("e = \n", e)

# batch_imagenes = np.random.randint(0,256, size=(1,8,8))
# print("batch_imagenes = \n", batch_imagenes)

# tensor6 = np.random.rand(2,2,2,2,2,2) # tensor de 6 dimensiones con números aleatorios entre 0 y 1
# print("tensor6 = \n", tensor6)

d = np.random.randint(0,100, size=(32,28,28))
print(d)

#broadcasting