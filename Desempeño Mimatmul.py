# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:15:34 2020

@author: Ale
"""

from scipy import rand
from time import perf_counter
from matplotlib import pyplot as plt 
import numpy as np

def mimatmul(A,B):
    
    Cantidady = (N,N)
    
    X = np.zeros(Cantidady)
    
    for i in range(0,len(A)):
        
        for j in range(0,len(A)):
            
            s = 0
        
            for k in range(0,len(A[i])):

                s += A[i][k]*B[k][j]
                X [i][j] = s
                
    if i is not j:
        print("Las matrices son de diferente dimensión en filas A y columnas B.")
        
    return X

# Para las corridas se realizó hasta N = 500 ya que con una matriz de mayor tamaño, se tomaba mucho tiempo!

Tamañodelamatriz = [2,5,10,15,20,30,40,50,60,100,200]
    
dt = []
memoria = []
    
Cantidadcorridas = 10

for numerocorrida in range(Cantidadcorridas):
    
    corrida = open(f"Corrida{numerocorrida}.txt","w")
    
    for N in Tamañodelamatriz:
        
         A = rand(N,N)
         B = rand(N,N)

         t1 = perf_counter()
    
         X = mimatmul(A,B)

         t2 = perf_counter()
    
         deltatiempo = t2 - t1
    
         memoria1 = 3*(N**2)*8
    
         print(f"Para un N = {N}")
    
         print(f"El tiempo entre ambos es {deltatiempo} s")
    
         print(f"La memoria utilizada es de {memoria1} bytes")
         print("--------------------------------------")
         
         dt.append(deltatiempo)
         memoria.append(memoria1)
         
         corrida.write(f"{N} {deltatiempo} {memoria1}\n")
         corrida.flush()

plt.figure()

plt.subplot(2,1,1)

x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]    
y1 = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10,]
yl = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10,]
yt = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

for i in range(Cantidadcorridas):
    
    memoriausada=[]
    tiempos = []
    archivos = (f"Corrida{i}.txt")
    apertura = open(archivos,'r')
    todas_las_lineas = apertura.readlines()
    
    for j in range(len(Tamañodelamatriz)):
        
        fila = []
        fila.append(todas_las_lineas[j])
        fila = fila[0].split(" ")
        tiempos.append(float(fila[1]))
        memoriausada.append(int(fila[2]))
        
    apertura.close()
    plt.loglog(Tamañodelamatriz,tiempos,"-o")
    
plt.xticks(x,[])
plt.yticks(y1,yl)
plt.grid(True) 
plt.ylabel("Tiempo Transcurrido (s)")
plt.title("Rendimiento A@B=X")   

plt.subplot(2,1,2)
plt.loglog(Tamañodelamatriz,memoriausada,"-o") 
plt.xticks(x,x,rotation=45)
plt.grid(True) 
plt.yticks(y2,yt)
plt.ylabel("Uso de Memoria")
plt.xlabel("Tamaño de la matriz (N)")
plt.axhline(y=16000000000, xmin=0.001, xmax=0.9999,color="red",ls="--")

plt.show()