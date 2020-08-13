# MCOC2020-P0

# Entrega 1:

* Mi computador (Alejandro Bello Castillo) 

* Marca/Modelo: Lenovo Legion Y520 

* Tipo: Notebook

* Año adquisición: 2017

* Procesador
  - Marca/Modelo: Intel Core i7-7700HQ 
  - Velocidad base: 2,8 GHz
  - Velocidad máxima: 3,8 GHz 
  - Número de núcleos: 4
  - Número de hilos: 8 
  - Arquitectura: Sistema operativo de 64 bits, procesador x64
  - Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2

* Tamaño de las cachés del procesador
  - L1: 256 kB
  - L2: 1,0 MB
  - L3: 6,0 MB 

* Memoria
  - Total: 16 GB
  - Tipo de memoria: DDR4
  - Velocidad: 2400 MHz
  - Número de (SO)DIMM: 2 

* Tarjeta gráfica 
  - Marca/Modelo: NVIDIA GeForce GTX 1050 4 GB 
  - Memoria dedicada: 4000 MB
  - Resolución: 1920x1080

* Disco 1: 
  - Marca: Seagate ST1000LM035-1RK172
  - Tipo: HDD
  - Tamaño: 1 TB
  - Particiones: 1
  - Sistema de archivos: NTFS

* Disco 2: 
  - Marca: NVMe SAMSUNG MZVLW128 
  - Tipo: SSD 
  - Tamaño: 128 GB
  - Particiones: 3
  - Sistema de archivos: NTFS

* RED/WIFI 

* Dirección MAC de la tarjeta wifi: 58-00-E3-F3-BE-09

* Dirección IP (Interna, del router): 192.168.0.241

* Dirección IP (Externa, del ISP): 192.168.0.1

* Proveedor internet: VTR Banda Ancha S.A.

# Entrega 2: 
## Desempeño Matmul
* Gráfico:

![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Gr%C3%A1fico%20python.png?raw=true)

* Preguntas: 

* ¿Como difiere del gráfico del profesor/ayudante?
  - En el caso del gráfico del tiempo transcurrido, existe una diferencia en los valores del inicio del programa (Con N=2), donde toma un mayor tiempo el gráfico presentado. Por otro lado, la variabilidad es en distintos N, siendo para el profesor en N [50,1000] y en el presentado N [20,200]. Finalmente, en el N = 50000 hay una relativa igualdad en el tiempo. En la memoria usada, existe una prácticamente igualdad en sus términos. (Notar que en el gráfico presentado, se llega hasta N = 5000, pues ante un mayor N, el tiempo en terminar las corridas era alto). 

* ¿A qué se pueden deber las diferencias?
  - Las diferencias se deben a la potencia de los computadores utilizados por el alumno y el profesor, teniendo carácteristicas un poco menos potentes en mi caso. Se debe a factores como la cantidad de núcleos, procesador (Generación) y la memoria RAM de cada computador, que según lo expuesto en clases por el profesor era de 32 GB vs el mío que posee 16 GB.
  
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - Se puede ver que el gráfico de memoria sí es lineal, esto se debe a que la memoria utilizada se realiza a través de una fórmula que variará en función del tamaño de matriz que se utiliza (En este caso N), y los bytes de almacenamiento, que son constantes y por lo tanto, no variará en función de la corrida que se realice, siempre obteniendose iguales datos. En cambio para el tiempo transcurrido, va a depender del procesador y la cantidad de procesos que se estén llevando a cabo en el mismo momento que se hace correr el programa. 

* ¿Qué versión de python está usando?
  - La versión utilizada es: 3.8 en Spyder 4.1.4

* ¿Qué versión de numpy está usando?
  - La versión utilizada es: 1.18.5 

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  - Según lo expuesto en la imagen, se puede observar el uso de los 8 procesadores. 
  
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Procesador.png?raw=true)

# Entrega 3: 
## Desempeño Mimatmul
* Gráfico:

![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Gr%C3%A1fico%20E3.png?raw=true)

* Preguntas: 

* ¿Como difiere del gráfico del profesor/ayudante?
  - En el caso del gráfico del tiempo transcurrido, existe una diferencia en los valores del inicio del programa (Con N=2), donde toma un mayor tiempo el gráfico mostrado por el ayudante, pues en ese caso, la relación al rededor del valor N=5 tiende a una linealidad, sin embargo el gráfico presentado, tiene por tendencia la linealidad del proceso a partir del primera corrida con los respectivos N que se definen en la entrega del archivo python, obviamente con algo de variabilidad entre corrida, pero tendiendo a un mismo trazo lineal.  
En la memoria usada, existe una prácticamente igualdad en sus términos. (Notar que en el gráfico presentado, se llega hasta N = 200, pues ante un mayor N, el tiempo en terminar las corridas era alto). 

* ¿A qué se pueden deber las diferencias?
  - Las diferencias se deben a la potencia de los computadores utilizados por el alumno y el profesor, teniendo carácteristicas un poco menos potentes en mi caso. Se debe a factores como la cantidad de núcleos, procesador (Generación) y la memoria RAM de cada computador, que según lo expuesto en clases por el profesor era de 32 GB vs el mío que posee 16 GB. Además de esto, se puede deber a la rapidez que tiene de reacción la CPU de cada computador, y obviamente que tan cargada está esta última, que variará linealmente en función del tiempo que toma cada corrida del programa.
  
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - Se puede ver que el gráfico de memoria sí es lineal, esto se debe a que la memoria utilizada se realiza a través de una fórmula que variará en función del tamaño de matriz que se utiliza (En este caso N), y los bytes de almacenamiento, que son constantes y por lo tanto, no variará en función de la corrida que se realice, siempre obteniendose iguales datos. En cambio para el tiempo transcurrido, si bien se ve cierta linealidad debido a que se crea una función con igualdad de parámetros para matrices de tamaño (N,N) igualmente dependerá de las características del pc como también las actividades que se están realizando en el momento. 

* ¿Qué versión de python está usando?
  - La versión utilizada es: 3.8 en Spyder 4.1.4

* ¿Qué versión de numpy está usando?
  - La versión utilizada es: 1.18.5 

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  - Según lo expuesto en la imagen, se puede observar el uso de los 8 procesadores. 
  
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/CPU.png?raw=true)

# Entrega 4:

*Preguntas:

*¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
 - Respuesta

*¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
 - Respuesta
