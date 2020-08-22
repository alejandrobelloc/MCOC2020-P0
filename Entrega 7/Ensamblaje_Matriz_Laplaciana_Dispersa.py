# -*- coding: utf-8 -*-

from numpy import zeros,double
import numpy as np
from scipy.sparse import lil_matrix

def matriz_laplaciana_dispersa(N,t=np.float32):
    
    A = lil_matrix((N,N))
    
    for i in range(N):
        
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i+1 == j:
                A[i,j] = -1
            if i-1 == j:
                A[i,j] = -1
    return A

# Comprobamos que esté bien y tome solo los valores distintos de 0 en la matriz: 
# X = matriz_laplaciana_dispersa(10)
# print(X)
# Está todo ok, da valores (1,0) - Valor ---> Lo que significa que toma la fila N°1 y la columna 0 con valor un "Y"