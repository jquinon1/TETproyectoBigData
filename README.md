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

### 2.4 Montarlos al HDFS

Una vez limpio los archivos procedemos a montarlos al HDFS

      $ hdfs -put articles*.csv <hdfs_folder>
