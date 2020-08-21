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
* Análisis de gráficos generales: 
 - Se puede observar que ambas funciones, tanto numpy como scipy no se notó una gran variación de rendimiento ni de uso de memoria, dando gráficos más bien parecidos. Esto se puede deber al método que usan ambos, que para el tiempo que demora con las características del computador como el procesador, ram, etc, tienen un efecto parecido. 
 
 - Respecto a la funciones True and False, se puede observar una mayor ganancia de desempeño y un menor uso de CPU en el caso True, esto es debido a que toma en consideración las Cachés del computador, pudiendo guardar alguna similitud de archivos para los distintos textos, lo que obtiene lo anteriormente mencionado. En el caso de False, esto no es así, partiendo de 0 el cálculo de cada matriz lo que conllevará una disminución de desempeño y un aumento de uso de la CPU, lo que es posible ver más adelante con los gráficos puestos.
 
* Preguntas:

* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
  - Se realiza mediante el método de Algebra Lineal que posee numpy, mediante cálculos con programación de bajo nivel, siendo numpy más eficiente y proactivo que scipy para este tipo de problemas de álgebra. Los posibles casos de inversión de matrices pueden ser diagonalización, propiedades de matrices, etc.

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
  - El paralelismo en la arquitectura del computador, es una función en la cual se permite realizar varias tareas al mismo tiempo, tomando diversos porcentajes de uso de la cpu en función de las tareas y la complejidad de realización que estas tienen. El caché busca la realización más rápida de algunas tareas que ya se han realizado antes, guardando estos datos para futuros usos. Debido a lo anterior, es que la cpu y el uso de caché en función de los casos que se van realizando, debería tomar un menor % de uso, para la última función que toma, es decir single,double,.. etc. 
  Si se observa como es la utilización de los cachés y la cpu, para cada caso (Caso I,II y III respectivamente), se puede ver lo siguiente: 
  
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/CPU%20CASO%20I.png?raw=true)
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/CPU%20CASO%20II.png?raw=true)
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/CPU%20CASO%20III.png?raw=true)

# Entrega 5:
* Acá se encuentra el gráfico para tan solo para una de las dos formas de realizar el sistema de ecuaciones, me faltó tiempo para el sgdo, tuve otra entrega en otro ramo el mismo día.. 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/E5.png?raw=true)

# Entrega 6:
* En la entrega número 6 se replicó lo que se hizo para la entrega 5, agregando los solver de scipy con algunas de sus opciones, estas son: 
  - Symmetric (Convierte la matriz A en una matriz simétrica y definida positiva)
  - Solver de scipy (Convierte la matriz A en la inversa de esta y realiza el sistema)
  - Invirtiendo la matriz a través del solver (Solver puro)
  - Overwrite (Sobreescribe datos, lo que en un inicio podría demorar, pero luego, toma menos tiempo; Mejora rendimiento)
* A partir de lo anterior, se graficó la perfomance de como afectaba al tiempo de ejecución los distintos solver y sus opciones, tanto en numpy y scipy, el gráfico se puede observar a continuación, el cual se realizó bajo 10 corridas llegando a un N máximo igual a 10.000.

![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B06/Entrega%206.png?raw=true)

* Como es observable, se puede ver una relativa similitud en los tiempos transcurridos para bajo tamaños de matrices (Entre 2 y 200) para luego separarse en dos lineas prácticamente lineales donde se va un tipo de solver con menos efectividad de tiempos, y el resto, convergiendo a valores similares con tiempos más eficientes. 

* Especificamente, en un inicio, el solver de numpy puro, sin necesidad de invertir la matriz, tomó una menor cantidad de tiempo, en cambio, el solver de scipy puro, tomó una mayor cantidad de tiempo de ejecución. 

* Si vemos el caso final, se observa que el solver de numpy con el método de inversión de la matriz (A ; A*x = b) es el que toma la mayor cantidad de tiempo ante grande tamaños de matrices, que en este caso es sobre N = 200, seguido por el solver de scipy, que ocupa el mismo método de resolución de sistema de ecuaciones matriciales. En cambio, los métodos que no realizan inversión directa de la matriz A. toman un tiempo similar llegando a un tiempo máximo de ejecución bajo matrices de N = 10.000 de 10 segundos. Esto es completamente esperable, pues al sistema le cuesta mucha más memoria y capacidad del procesador el realizar la inversión de matrices grandes, pues la aproximación de valores van tomando grandes errores a medida que se aumenta este último valor, en cambio, solver directos a través de librerias como numpy y scipy, optimizan las operaciones. Además de esto, al tener la matriz laplaciana tenemos grandes cantidades de valores con 0, cosa que al invertir las matrices, tomará más tiempo, siendo que estos valores son inutiles para el cálculo, ya que quedarán como 0 de igual manera para invertir la matriz. 

* También podemos observar el uso de la cpu en dos programas, tanto de HWMONITORPRO y el administrador de tareas de windows, junto con los núcleos del computador (4): 

![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B06/CPU%20y%20n%C3%BAcleos.png?raw=true)
![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B06/CPU%20y%20su%20%25%20de%20uso.png?raw=true)

* En el primer gráfico, se puede observar el gran uso de ambas caracteristicas del computador, exigiendo tanto los hilos del procesador (A valores no menos del 21% y máximos de 84%) como también los núcleos (Valores del 3393 MHz, casi en el máximo de su capacidad).

* El segundo gráfico es para mostrar los bumps que posee la CPU y su % de uso, que se puede deber a lo anteriormente expuesto, como por ejemplo el overwrite de scipy con bumps más bajos y la inversión de matrices para los bumps más elevados. 

* Fin.

## Entrega 7:
# Complejidad algoritmica de MATMUL
  - Gráfico: 
* Diferencias entre las matrices llenas y dispersas.
  - Respuesta.. 
  
* Complejidad asintótica para el ensamblado y solución en ambos casos.
  - Respuesta.. 
  
* Como afecta el tamaño de las matrices al comportamiento aparente.
  - Respuesta..
  
* Son estables las corridas (Número de corridas = 5). 
  - Respuesta

# Complejidad algoritmica de SOLVE
  - Gráfico: 
* Diferencias entre las matrices llenas y dispersas.
  - Respuesta.. 
  
* Complejidad asintótica para el ensamblado y solución en ambos casos.
  - Respuesta.. 
  
* Como afecta el tamaño de las matrices al comportamiento aparente.
  - Respuesta..
  
* Son estables las corridas (Número de corridas = 5). 
  - Respuesta

