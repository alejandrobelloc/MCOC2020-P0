# -*- coding: utf-8 -*-

from numpy import zeros,double
import numpy as np

def matriz_laplaciana_llena(N, dtype=double):
    
    Matrizlp = zeros((N,N), dtype=double)
    
    for i in range (N):
        
        for j in range (N):
            
            if i==j:
                Matrizlp[i,j]=2
                
            if i+1==j:
                Matrizlp[i,j]=-1
                
            if i-1==j:
                Matrizlp[i,j]=-1
                
    return Matrizlp

# Está matriz llena ya fue comprobada en la entrega N°6 ; Donde se ve claramente que toma todos los valores propios de la matriz "N", incluyendo 0s.