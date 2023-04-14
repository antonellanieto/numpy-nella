import numpy as np

#ubicar fila y columna
matriz_ubicar = np.arange(24).reshape(4, 6)
print(matriz_ubicar [3, 4]) # 22

#ordenar de manera ascendente
m1 = np.array([100, 2, 92, 3, 77])
print(np.sort(m1))

#elevar elementos a una potencia
m2 = np.array([2, 3])
print(np.power(m2, 3)) #o print(np.array(mp2**3)

#clasificarlos si son mayores a tal valor, devuelta True o False
m3 = np.array([8, 9, 10, 11])
print(np.array(m3 <= 9))

#encontrar valor maximo y el minimo en una matriz
m4 = np.array([3, 4, 5, 6, 7])
print(np.array(m4.max()))
print(np.array(m4.min()))

#concatenar matrices
m5 = np.array([3, 5, 8])
m6 = np.array([9, 22, 5])
print(np.concatenate((m5, m6)))


#numero aleatorios con una matriz de una dimensión
m7 = np.random.randint(10, size=5) #10 es dentro de los numeros aleatorios 0 al 10 y size cuántos te va a tirar
print(m7)

#numeros aleatorios con una matriz de dos dimensiones
m8 = np.random.randint(10, size=(3, 3))
print(m8)

#numeros aleatorios a partir de elementos que pueden ser decimales, rand sin el int
m9 = np.random.rand(2, 2)
print(m9)

#extraer o devolver 1 valor de la matriz de 1 dimensión
m10 = np.random.choice([5, 9, 8, 5, 10])
print(m10) 