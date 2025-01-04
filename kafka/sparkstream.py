from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Kafka topic and HDFS details
KAFKA_TOPIC = "users"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9093"
HDFS_OUTPUT_PATH = "hdfs://namenode:8020/user/hive/warehouse/users"

# Define schema for incoming Kafka data
schema = StructType([
    StructField("id", StringType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("state", StringType(), True),
    StructField("street_address", StringType(), True),
    StructField("postal_code", StringType(), True),
    StructField("city", StringType(), True),
    StructField("country", StringType(), True),
    StructField("latitude", StringType(), True),
    StructField("longitude", StringType(), True),
    StructField("traffic_source", StringType(), True),
    StructField("created_at", StringType(), True)
])

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaToHDFSToHiveStreaming") \
    .config("spark.sql.catalogImplementation", "hive") \
    .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
    .enableHiveSupport() \
    .getOrCreate()

# Read data from Kafka topic
df_kafka = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON data
df_parsed = df_kafka.selectExpr("CAST(value AS STRING)").select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

# Write to HDFS as Parquet
def write_to_hdfs(batch_df, _):
    # Write the batch data to HDFS
    batch_df.write \
        .mode("append") \
        .parquet(HDFS_OUTPUT_PATH)

# Start the stream processing
query = df_parsed.writeStream \
    .foreachBatch(write_to_hdfs) \
    .outputMode("append") \
    .start()

query.awaitTermination()
