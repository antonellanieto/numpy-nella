import numpy as np

m = np.array([[1, -1, 2],[3, 2, 0]])
print(m)

print("")
#matriz trapsuesta
#se obtiene cambiando sus filas por columnas o viceversa.
m1 = np.array([[1, 2, 3]])
print(m1)
print(np.transpose(m1))


#sistema de ecuaciones
#resolver ecuación Ax = b 

A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
b = np.array([[-3], [5], [-2]])
print(np.transpose(b))

x = np.linalg.solve(A,b) #calculo
print(x)
print(np.allclose(np.dot(A,x), b)) #esto tiene ser verdadero, si el resultado es correcto de x


