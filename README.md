#  Proyecto 04 - ST0263 - Clústering de documentos a partir de métricas de similitud basado en Big Data

Integrantes del grupo:

* Juan Pablo Londoño Botina - jlondo96@eafit.edu.co

* Jhonatan Quiñonez Avila   - jquinon1@eafit.edu.co

* Wilfer Salas Gonzales     - wsalasg@eafit.edu.co

## 1. Descripción del proyecto:
Este proyecto hace parte de la asignatura Tópicos Especiales en Telemática. Este consiste en; por medio de Big Data agrupar un conjunto de documentos (clustering) utilizando el framework Spark y haciendo uso de sus librerias de Machine Learning: K-Means y TF-IDF, para las métricas de similaridad entre documentos.

## 2. Modo de ejecución:
Para la ejecucion de este proyecto se deben seguir los siguientes pasos

### 2.1. Descargar el datasets desde el siguiente enlace

      https://drive.google.com/open?id=1-HBV1E0Vr0BpPsWSmQUX9h76faotEap6

### 2.2. Envio de archivos

Una vez descargados procedemos a enviarlos a traves de consola a la maquina donde se hara el procesamiento, en nuestro caso la proporcionada por el facilitador del curso

      $ scp all-the-news.zip <user>@<machine_ip>:~

### 2.3. Ahora procedemos a descomprimirlos

      $ unzip all-the-news.zip

### 2.3. Limpieza

En este punto debemos realizar un cleaning de la data, ya que esta viene con ciertos saltos de linea y caracteres especiales que no queremos que entren en el criterio de clustering.
Para este ejecutamos desde linea de comando los siguiente

      $ python verify.py

Este script realiza la limpieza respectiva de todos los archivos descomprimirdos.

### 2.4. Montarlos al HDFS

Una vez limpio los archivos procedemos a montarlos al HDFS

      $ hdfs -put articles*_*.csv <hdfs_folder>

### 2.5. Ejecutar

      $ spark-submit  --master yarn --deploy-mode cluster --executor-memory <memoriaGB>G --num-executors <numExecutors> kmeans.py <hdfs_input_directory> <k> <iterations> <hdfs_output_directory>
      
O para hacerlo de manera local
      
      $ spark-submit --executor-memory <memoriaGB>G kmeans.py <hdfs_input_directory> <k> <iterations> <hdfs_output_directory>

### 2.6. Obtener resultados

Una vez ejecutado el script debe obtener los resultados para esto

      $ hdfs dfs -get <hdfs_output_directory>/*.csv

Y lo renombramos para facilidad

      $ mv part*.csv result.csv

 !!! IMPORTANTE COLOCAR ESE NOMBRE

 Ahora para finalizar ejecutamos el script plot.py que nos devolvera k imagenes y k archivos, las imagenes conteneran palabras claves del topico de las noticias pertenecientes al cluster, y los archivos, el titulo de las noticias pertenecientes al cluster

      $ python plot.py

## 3. Algoritmos utilizados:

* HashingTF: HashingTF es un Transformer que toma conjuntos de términos y los convierte en vectores de características de longitud fija. En el procesamiento de texto, un "conjunto de términos" puede ser una bolsa de palabras. HashingTF utiliza el truco de hash. Una característica sin formato se mapea en un índice (término) aplicando una función hash. La función hash utilizada aquí es MurmurHash 3.
* TF-IDF (Term frequency-inverse document frequency): Tf-idf (del inglés Term frequency – Inverse document frequency), frecuencia de término – frecuencia inversa de documento (o sea, la frecuencia de ocurrencia del término en la colección de documentos), es una medida numérica que expresa cuán relevante es una palabra para un documento en una colección. Esta medida se utiliza a menudo como un factor de ponderación en la recuperación de información y la minería de texto. El valor tf-idf aumenta proporcionalmente al número de veces que una palabra aparece en el documento, pero es compensada por la frecuencia de la palabra en la colección de documentos, lo que permite manejar el hecho de que algunas palabras son generalmente más comunes que otras.
* K-means: Algoritmo de agrupamiento, se requiere un numero de clusters a generar y una matriz que contiene la frencuencia de terminos obtenida de un conjunto de datos.

## 4. Requisitos:

* Cluster con Spark (>= 2.1.1.2.6.1.0-129)
* Java Development Kit (>= 1.8.0_144)
* Python (>= 3.6.2)
* Pyspark
* Hadoop (>= 2.7.3.2.6.1.0-129)
* Numpy
* PIL
* WordCloud

## 5. Referencias:

* "Clustering with K-Means with Spark and MLlib"                                      - http://timothyfox.net/?p=15
* "TF-IDF, HashingTF and CountVectorizer"                                             - https://mingchen0919.github.io/learning-apache-spark/tf-idf.html
* "TF-IDF with Spark for the Kaggle popcorn competition"                              - https://github.com/logicalguess/tf-idf-spark-and-python
* "Feature Extraction and Transformation - RDD-based API - Spark 2.2.0 Documentation" - https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html
* "Extracting, transforming and selecting features"                                   - https://spark.apache.org/docs/2.3.0/ml-features.html
