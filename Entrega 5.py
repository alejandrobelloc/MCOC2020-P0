# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:15:34 2020

@author: Ale
"""

from time import perf_counter
import matplotlib.pyplot as plt
import sys
from numpy import zeros, float32
import numpy as np


from scipy import linalg

############## ¡IMPORTANTE! ############### 
# Este código es para toda la entrega, para corregir favor cambiar en la linea N19 dtype= np.single (Por Half, Single, Double y Longdouble)
############## ¡IMPORTANTE! ############### 

def matriz_laplaciana(N, dtype=float32):
    
    Matrizlp = zeros((N,N), dtype=np.single)
    
    for i in range (N):
        
        for j in range (N):
            
            if i==j:
                Matrizlp[i,j]=2
                
            if i+1==j:
                Matrizlp[i,j]=-1
                
            if i-1==j:
                Matrizlp[i,j]=-1
                
    return Matrizlp

Tamañodelamatriz = [2,5,10,15,20,30,40,50,60,100,200,500,1000,2000,3000]
    
dt = []
    
Cantidadcorridas = 1


for numerocorrida in range(Cantidadcorridas):
    
    corrida = open(f"Corrida{numerocorrida}.txt","w")
    
    for N in Tamañodelamatriz:
        
         ML = matriz_laplaciana(N)
         B = np.ones(N)
         
         t1 = perf_counter()
    
         MLinv = np.linalg.inv(ML)
         MLinvB = MLinv@B

         t2 = perf_counter()
    
         deltatiempo = t2 - t1
         
         ML = matriz_laplaciana(N)
         B = np.ones(N)
         
         t1 = perf_counter()
    
         MLinvB = np.linalg.solve(ML,B)

         t2 = perf_counter()
    
         deltatiempo = t2 - t1
    
         print(f"El tiempo entre ambos es {deltatiempo} s")
    
         print("--------------------------------------")
         
         dt.append(deltatiempo)
         
         corrida.write(f"{N} {deltatiempo}\n")
         corrida.flush()

plt.figure()

plt.subplot(2,1,1)

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]    
y1 = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10,]
yl = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
yt = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

for i in range(Cantidadcorridas):
    
  
    tiempos = []
    archivos = (f"Corrida{i}.txt")
    apertura = open(archivos,'r')
    todas_las_lineas = apertura.readlines()
    
    for j in range(len(Tamañodelamatriz)):
        
        fila = []
        fila.append(todas_las_lineas[j])
        fila = fila[0].split(" ")
        tiempos.append(float(fila[1]))
        
    apertura.close()
    plt.loglog(Tamañodelamatriz,tiempos,"-o",color="yellow",label="linalg.inv")



plt.xticks(x,x,rotation=45)
plt.yticks(y1,yl)
plt.grid(True) 
plt.ylabel("Tiempo Transcurrido (s)")
plt.xlabel("Tamaño de la matriz N")
plt.title("Rendimiento A@B=X")   
plt.legend()
plt.show()








