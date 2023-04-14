import numpy as np


# Matriz dos dimensions
matriz_dos_d = np.array([[1, 2, 3],[4, 5, 6]])
print(matriz_dos_d)

#Lista para matriz 
lista_para_matriz = [8, 9, 10]
matriz_de_lista = np.array(lista_para_matriz)
print(matriz_de_lista)

#lista de dos dimensiones
lista_dos_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_de_lista_dos_d = np.array(lista_dos_d)
print(matriz_de_lista_dos_d)

#generar un rango
m = np.arange(15).reshape(3, 5) #arange cantidad de valores, reshape columnas y filas, matriz de 3 x 5 en este caso
#si no se le agrega reshape lo deja en 1 dimensión
print(m)
