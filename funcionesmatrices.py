import numpy as np




m = np.arange(20).reshape(4, 5)
print(m) 
# print(m.shape) shape te muestra los valores de reshape, te muestra las filas y columnas de la matriz
# print(m.ndim) numero de ejes o dimensiones que posee la matriz. 
# print(m.size) numero total de elementos de la matriz


# matriz de puros ceros
ceros = np.zeros((3, 4))
print(ceros)

#matriz de 3 dimensiones
tres_dimensiones = np.arange(24).reshape(2, 3, 4) # la tercera dimension es el primer valor dentro de reshape
# el numero dos, indica la cantidad de matrices. Luego vienen las filas y columnas,más de dos matrices se considera
#3 dimensiones. 


