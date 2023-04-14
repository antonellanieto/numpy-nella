import numpy as np

# axis 1 para columnas, axis 0 filas

#encontrar minimo o máx
m = np.array([[1, 2, 3], [4, 5,6], [7,8,9]])
print(np.amin(m)) #si le agrego 1 me da el minimo de cada fila, si le agrego 0 da el minimo de cada columna
print(np.amax(m))

#encontrar rango, rango= maxx - minx
print(np.ptp(m)) #8, 9 - 1 = 8
print(np.ptp(m, axis=1)) #segund la columna cada min

# en estadística, percentil es un valor que sirve más que nada para comparar un conjunto (en éste caso ordenado) de datos
# tiene una fórmula:
# percentiles = q(n + 1) / 100 
# q = percentil a calcular (entre 0 a 100 generalmente)
# n = total de datos
# ésta fórmula funciona sólamente cuando los elementos de la matriz son impar, el total n = impar
#si n = par, aplicar ésta fórmula:
# percentiles = q x n / 100

print(np.percentile(m, 50)) 

# mediana = (n + 1) / 2
print(np.median(m))
print(np.median(m, axis=0)) #tomando en cuenta las col, axis = 0


#media aritmética = x1 + x2 + .....xn / n
#suma de cada uno de los datos, dividos entre el total de los elementos
print(np.mean(m)) # 1 +2 +3 +4 +5+ 6+ +7 +8 +9 / 9


#el promedio ponderado = x1 * p1 + ..... xn* pn / Σp
# p representa un determnado peso, que puedes asignar pero puede ser uno por defecto
#se multiplica al elemento de la matriz y se divide entre sumatoria de los pesos
m1 = np.array([1, 2, 3, 4, 5, 6])
print(np.average(m1)) #por defecto se determina peso = 1 si no se indica, 1 por el peso(1*1),  más el segundo elemento que
# es 2, 1+2. Luego se multiplica por el peso nuevamente que es 1. Y asi se suma sucesivamente cada elemento * el peso
#se divide entre la sumatoria de los pesos que es 1 cada peso, por cada elemento, 6. el total dividido 6.

# desviación estándar 
# std = sqrt(mean(abs(x-x.mean())**2))
print(np.std(m1))
