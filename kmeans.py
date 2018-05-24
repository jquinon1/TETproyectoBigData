import sys
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession

def kmeans(params):
    path = params[0]
    k = int(params[1])
    iterations = int(params[2])
    target_dir = params[3]

    try:
        # Creating session
        spark_session = SparkSession.builder.appName("project4-jwj").getOrCreate()

        # loading the files from hdfs ang getting a DataFrame
        data = spark_session.read.format("csv").option("header","true").load("{}/*.csv".format(path))
        #data.show()

        # Breaking the content column into individual words
        tokenizer = Tokenizer(inputCol="content",outputCol="Words")
        tokenized = tokenizer.transform(data)
        #tokenized.show()
        # Removing stop words
        remover = StopWordsRemover(inputCol="Words",outputCol="Filtered")
        removed = remover.transform(tokenized)
        #removed.show()

        # Term frecuency - inverse document frecuency
        hashingTF = HashingTF(inputCol="Filtered",outputCol="rawFeatures",numFeatures=200000)

        # Getting the frecuency term vector to try to get k and train kmeans
        featurizedData = hashingTF.transform(removed)
        #featurizedData.show()

        idf = IDF(inputCol="rawFeatures",outputCol="features",minDocFreq=5)
        idfModel = idf.fit(featurizedData)
        rescaledData = idfModel.transform(featurizedData)
        rescaledData.show()
        # Train KMeans
        #kmean = KMeans().setK(k).setMaxIter(iterations).fit(rescaledData)
    except Exception as e:
        print(str(e),file=sys.stderr)
        sys.exit(1)






# Execution
if __name__ == "__main__":
    if len(sys.argv) < 4: # verify number of params
        print("Uso: spark-submit {} <hdfs_input_directory> <k> <iterations> <hdfs_output_directory>".format(sys.argv[0]),file=sys.stderr)
        print("                     :   hdfs folder must be i absolute path example hdfs:///user/jquinon1/datasets/project",file=sys.stderr)
        sys.exit(1)
    kmeans(sys.argv[1:])
