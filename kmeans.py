import sys
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession
from pyspark import SparkContext

def kmeans(params):
    path = params[0]
    k = int(params[1])
    iterations = int(params[2])
    target_dir = params[3]

    # Creating session
    try:
        spark_session = SparkSession.builder.appName("project4-jwj").getOrCreate()

        data = spark_session.read.format("csv").option("header","true").load("{}/*.csv".format(path))
        data.show()

    except Exception as e:
        print(str(e),file=sys.stderr)
        sys.exit(1)






# Execution
if __name__ == "__main__":
    if len(sys.argv) < 4: # verify number of params
        print("Uso: spark-submit {} <hdfs_input_directory> <k> <iterations> <hdfs_output_directory>".format(sys.argv[0]),file=sys.stderr)
        print("hdfs folder must be i absolute path example hdfs:///user/jquinon1/datasets/project",file=sys.stderr)
        sys.exit(1)
    kmeans(sys.argv[1:])
