import numpy as np

#axis(eje) controla el parámetro de cada función, cuando se aplique la palabra axis
# axis 1 para columnas, axis 0 filas

#suma numérica con el eje en 0, matriz dos dimensiones
m = np.array([[0, 1, 2],[4, 2, 3]])
print(m)
print(np.sum(m, axis=0)) #suma de elementos en dirección axis 0, para abajo: 0+4, 1+2, 2+3


#concatenar con eje axis en matriz dos dimensiones
m1 = np.array([[1, 1], [1, 1]])
m2 = np.array([[8, 8], [8, 8]])
print(np.concatenate([m1, m2], axis=0)) #cambia de forma si el eje esta cero o 1

#concatenar una matriz de una dimensión funciona con dos matrices de una dimensiones, concatenando con eje en 0 únicamente
m3 = np.array([1, 1])
m4 = np.array([8, 8])
print(np.concatenate([m3, m4], axis=0))
