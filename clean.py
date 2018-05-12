#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("cleaning-data").getOrCreate()

data = [('Consecutive',1),('Id',2),('Title',3),('Publication',4),('Author',5),('Date',6),('Year',7),('Month',8),('Url',9),('Content',10)]
# df = sparkSession.createDataFrame(data,header='true')

# Read from HDFS
df_load1 = sparkSession.read.csv('hdfs:///user/jquinon1/datasets/project/articles1_cleaned.csv',header='true')
df_load2 = sparkSession.read.csv('hdfs:///user/jquinon1/datasets/project/articles2_cleaned.csv',header='true')
df_load3 = sparkSession.read.csv('hdfs:///user/jquinon1/datasets/project/articles3_cleaned.csv',header='true')
df_load.count()
