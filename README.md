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

# Entrega 7:
## Complejidad algoritmica de MATMUL 
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Matmul(A%40B)%20%3B%20Matriz%20Llena.png?raw=true)
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Matmul(A%40B)%20%3B%20Matriz%20Dispersa.png?raw=true)
  
* Diferencias entre las matrices llenas y dispersas.
  - Se puede observar dentro de ambos gráficos que en la matriz llena, hay una leve mejora en el tiempo de ensamblado versus la matriz dispersa, teniendo diferencias pequeñas, pero siempre menores para las distintas corridas (N=5), luego se puede observar que en la matriz llena, existen distintos bumps en valores pequeños de tamaño de matrices, cosa que en la matriz dispersa no pasa, teniendo un comportamiento practicamente 'lineal'. En el caso del tiempo de solución se puede ver una mejora también en el mismo orden que el anterior, sin embargo a largo plazo con matrices grandes, el tiempo de solución es mucho mayor para la matriz llena avanzando de manera prácticamente cuadrática vs practicamente una linea recta del tiempo de solución, tomando valores cercanos al 1ms en la matriz dispersa.
  
* Complejidad asintótica para el ensamblado y solución en ambos casos.
  - Para el caso de la matriz llena: El ensamblado, cuando N tiende a infinito al observar las pendientes de los distintos N(2,3,4), yo diría que este esta tendiendo a un N cubo. A la solución, yo diría que y se puede observar claramente que este está tendiendo a un N3 de igual manera que el anterior.
  - Para el caso de la matriz dispersa: El ensamblado tiende de manera clara a N cuadrado, convergiendo practicamente al mismo valor ante N tendiendo a infinito. Para el caso de la solución se puede observar que tiende a una constante, la cual es representada mediante la linea azul. 
* Como afecta el tamaño de las matrices al comportamiento aparente.
  - En el caso de la matriz llena, podemos observar que a medida que aumenta el tamaño de matriz N, aumenta el tiempo de ejecución del programa, esto es visiblemente cierto ante hipotesis previas que se pueden realizar antes de correr el programa, pues al computador le cuesta más la ejecución y el calculo, al tener que aproximar valores, errores, etc. Para el caso de la matriz dispersa, es fácil ver que en el caso del ensamblado, ocurre lo que uno esperaría, que existe una relación directa entre ambos factores, sin embargo, para el tiempo de ejecución ocurre algo relativamente anormal, si es que uno no entiende lo que realiza la matriz dispersa, esperaria una respuesta como la que mencione, pero debido a que este comando lo que hace es "desactivar" todas las diagonales y valores que toman el 0, hace que el programa sea muy efectivo, y no tome en consideración diversos valores que si lo hace el caso de matriz llena, optimizando el cálculo del Matmul entre A y B. 
  
* Son estables las corridas (Número de corridas = 5). 
  - Para la matriz llena, tanto en el tiempo ensamblado como en el de solución, se puede observar que la gran mayoria de las corridas convergen a un mismo valor a lo largo del tamaño de la matriz, sin embargo se observan pequeños bumps ante matrices de bajos tamaños, en valores cercanos al 0 hasta el 100, sin embargo para tamaños más grandes, sí convergen al mismo valor. Para la matriz dispersa, si se puede observar una estabilidad en función del tamaño de matriz, tomando los mismos valores en función del gráfico y el tiempo que se está tomando. 

## Complejidad algoritmica de SOLVE
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Solve(A%2Cb)%20%3B%20Matriz%20Llena.png?raw=true)
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Solve(A%2Cb)%20%3B%20Matriz%20Dispersa.png?raw=true)
* Diferencias entre las matrices llenas y dispersas.
  - En este caso, se puede observar que comienza de manera más rápida el solve de la matriz llena, con diferencias bajas entre ambos métodos, a su vez, a medida que aumentamos el tamaño de matriz, también tiene una mayor rapidez la matriz llena, tomando en consideración, el TIEMPO DE ENSAMBLADO, practicamente teniendo comportamientos convergentes para todas las corridas. Para el tiempo de solución de ambos métodos de matrices, se puede observar lo mismo que lo anterior, es decir, la matriz llena comienza más rápido ante valores pequeños de tamaño de matrices, sin embargo a medida que aumentamos el tamaño de matriz, se puede observar que el tiempo de solución es menor la matriz dispersa vs la matriz llena. (En baja cantidad de diferencia)
  
* Complejidad asintótica para el ensamblado y solución en ambos casos.
  - Para el caso de la matriz llena: El ensamblado, cuando N tiende a infinito al observar las pendientes de los distintos N(2,3,4), yo diría que este esta tendiendo a un N cuadrado. A la solución, yo diría que y se puede observar claramente que este está tendiendo a un N cubo al tender N a infinito.
  - Para el caso de la matriz dispersa: El ensamblado tiende de manera clara a N cuadrado, convergiendo practicamente al mismo valor ante N tendiendo a infinito. Para el caso de la solución se puede observar que tiende a N, la cual es representada mediante la linea amarilla, que avanza como una función y = x.  
  
* Como afecta el tamaño de las matrices al comportamiento aparente.
  - En este caso, tanto para matrices llenas y dispersas se observa un aumento lineal del tiempo tanto de ejecución como de ensamblado ante el aumento del tamaño de la matriz, sin embargo a simple vista, es posible analizar que el aumento (pendiente) existente, es menor en el caso de la matriz dispersa, esto es debido a lo anteriormente mencionado, además de posibles programas que uno estuviese trabajando al mismo tiempo que corría spyder (Python).
  
* Son estables las corridas (Número de corridas = 5). 
  - Se puede observar que las corridas de la matriz llena si son estables en función del tamaño de la matriz, a excepción del tiempo de solución ante bajos N, donde se observan unos pequeños bumps en el tamaño de alrededor N = 0 ; N = 30, sin embargo, después de sobre pasar esto, convergen a valores similares. En el caso de la matriz dispersa, se puede observar que hay practicamente una estabilidad completa en las corridas que se dieron para este caso (N=5), convergiendo todas a valores practicamente iguales. 

## Complejidad algoritmica de INV
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Inv(A)%20%3B%20Matriz%20Llena.png?raw=true)
  ![alt text](https://github.com/alejandrobelloc/MCOC2020-P0/blob/master/Entrega%20N%C2%B07/Inv(A)%20%3B%20Matriz%20Dispersa.png?raw=true)
* Diferencias entre las matrices llenas y dispersas.
  - Se puede observar que en el caso de tiempo de ensamblado, la matriz llena vs la matriz dispersa, la primera se demora menos que la segunda ante valores muy pequeños de N (Alrededor de 200), para luego tender a demorarse practicamente lo mismo, sin embargo al llegar al tamaño de matrices muy altas, demorarse más la matriz dispersa. En el caso del tiempo de solución, se puede observar que la matriz llena es más rápida en la resolución de la inversión de la matriz A, sin embargo después toma una pendiente de aumento de tiempo muy baja hasta el N = 500, por lo que el tiempo de la matriz dispersa lo llega a alcanzar para finalmente, tomar valores de solución similares ante tamaños grandes de matrices. 
  
* Complejidad asintótica para el ensamblado y solución en ambos casos.
  - Para el caso de la matriz llena: El ensamblado, cuando N tiende a infinito al observar las pendientes de los distintos N(2,3,4), yo diría que este esta tendiendo a un N cuadrado. A la solución, yo diría que y se puede observar claramente que este está tendiendo a un N cubo al tender N a infinito.
  - Para el caso de la matriz dispersa: El ensamblado tiende de manera clara a N cuadrado, convergiendo practicamente al mismo valor ante N tendiendo a infinito. Para el caso de la solución se puede observar que tiende a N cuadrado, la cual es representada mediante la linea verde, que avanza como una función y = x2. 
  
* Como afecta el tamaño de las matrices al comportamiento aparente.
  - En este caso, tanto para matrices llenas y dispersas se observa un aumento lineal del tiempo tanto de ejecución como de ensamblado ante el aumento del tamaño de la matriz, sin embargo a simple vista, es posible analizar que el aumento (pendiente) existente, es menor en el caso de la matriz dispersa, esto es debido a lo anteriormente mencionado, además de posibles programas que uno estuviese trabajando al mismo tiempo que corría spyder (Python), ocurriendo lo mismo que en el punto de SOLVE. 
  
* Son estables las corridas (Número de corridas = 5). 
  - Para el caso de la matriz llena, se puede observar una baja estabilidad ante tamaños de matrices pequeños tanto en su tiempo de ensamblado como también en el tiempo de solución, esto está pasando en N = 0 y N = 80, para luego, llegar a una manera completamente convergente ante aumento de valores del tamaño de la matriz N. En el caso de la matriz dispersa, en ambos casos existe una completa linealidad en el aumento del tiempo en función del tamaño N, donde no es posible captar a simple vista pequeños incrementos de tiempo en diferentes números de corridas. 
