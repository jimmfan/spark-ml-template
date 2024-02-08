
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("ExplainExample").getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([(1, "foo"), (2, "bar"), (2, "bar"), (3, "baz")], ["id", "value"])

# Operation
filtered_df = df.filter(df.id > 1).distinct()
filtered_df.explain()
# For more detailed information
filtered_df.explain("extended")