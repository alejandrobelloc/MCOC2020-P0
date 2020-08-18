# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:15:34 2020

@author: Ale
"""

from time import perf_counter
import matplotlib.pyplot as plt
from numpy import zeros, float32
import numpy as np
import scipy.linalg as splinalg
import numpy.linalg as nplinalg

def matriz_laplaciana(N, dtype=float32):
    
    Matrizlp = zeros((N,N), dtype=float32)
    
    for i in range (N):
        
        for j in range (N):
            
            if i==j:
                Matrizlp[i,j]=2
                
            if i+1==j:
                Matrizlp[i,j]=-1
                
            if i-1==j:
                Matrizlp[i,j]=-1
                
    return Matrizlp

Tamañodelamatriz = [2,5,10,15,20,30,40,50,60,100,200,500,1000,2000,3000,5000,10000]
    
Cantidadcorridas = 10

# Como se enseño en ayudantia, dejamos una lectura y creación de archivos solo en 1 linea que contenga ambas 'listas' según el N.

nombres = ["MLinvBnp.txt", "MLinvBnpsolve.txt", "MLinvBspsolve.txt", "MLinvBsp.txt", "MLinvBspsym.txt", "MLinvBspow.txt"]
archivos = [open(nombre,"w") for nombre in nombres]
    
for N in Tamañodelamatriz:
    
    dt = np.zeros((Cantidadcorridas,len(archivos)))
    
    for k in range(Cantidadcorridas):
      
      # Archivo MLinvBnp:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinv = nplinalg.inv(ML)
      MLinvB = MLinv@B

      t2 = perf_counter()

      deltatiempo = t2 - t1
      dt[k][0] = deltatiempo

      # Archivo MLinvBnpsolve:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinvB = nplinalg.solve(ML,B)

      t2 = perf_counter()
    
      deltatiempo = t2 - t1
      
      dt[k][1] = deltatiempo
      
      # Archivo MLinvBspsolve:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinvB = splinalg.solve(ML,B)

      t2 = perf_counter()
    
      deltatiempo = t2 - t1
      
      dt[k][2] = deltatiempo          

      # Archivo MLinvBsp:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinv = splinalg.inv(ML)
      MLinvB = MLinv@B

      t2 = perf_counter()

      deltatiempo = t2 - t1
      dt[k][3] = deltatiempo
      
      # Archivo MLinvBspsym:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinv = splinalg.solve(ML,B,sym_pos = False)

      t2 = perf_counter()

      deltatiempo = t2 - t1
      dt[k][4] = deltatiempo
      
      # Archivo MLinvBspow:
      ML = matriz_laplaciana(N)
      B = np.ones(N)
         
      t1 = perf_counter()
    
      MLinv = splinalg.solve(ML,B,overwrite_a = False)

      t2 = perf_counter()

      deltatiempo = t2 - t1
      dt[k][5] = deltatiempo
                 
    dt_mean = [np.mean(dt[:,j]) for j in range(len(archivos))]
    
    for j in range(len(archivos)):
        
        archivos[j].write(f"{N} {dt_mean[j]}\n")
        archivos[j].flush()

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]    
y1 = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10,]
yl = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
yt = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

plt.figure()

for nombre in nombres: 
    
    data = np.loadtxt(nombre)
    Tamañodelamatriz = data[:,0]
    dt = data[:,1]

    plt.loglog(Tamañodelamatriz,dt,"-o",label=nombre)
    plt.xticks(x,x,rotation=45)
    plt.yticks(y1,yl)
    plt.grid(True) 
    plt.ylabel("Tiempo Transcurrido (s)")
    plt.xlabel("Tamaño de la matriz N")  

plt.subplot(1,1,1)
plt.tight_layout()
plt.legend()
plt.show()
plt.savefig('imagen.png',dpi=500)











