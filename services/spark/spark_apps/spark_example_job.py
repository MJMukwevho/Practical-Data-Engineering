import pyspark.sql.functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example spark job").getOrCreate()


data = [("mukovhe", "mukwevho", "400"), ("vhugala", "ratombo", "6000")]
columns = ["name", "surname", "age"]

spark_df = spark.createDataFrame(data, columns)

spark_df.show()
