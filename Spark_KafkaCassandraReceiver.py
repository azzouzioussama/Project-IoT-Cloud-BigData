from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession \
    .builder \
    .appName("KafkaToCassandra") \
    .config("spark.cassandra.connection.host", "localhost") \
    .config("spark.cassandra.connection.port", "9042") \
    .config("spark.cassandra.auth.username", "cassandra_username") \
    .config("spark.cassandra.auth.password", "cassandra_password") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_sentimentPred") \
    .load() \
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write the streaming DataFrame to Cassandra using foreachBatch
query = df \
    .writeStream \
    .foreachBatch(lambda batch_df, epoch_id: batch_df.write \
                  .format("org.apache.spark.sql.cassandra") \
                  .option("keyspace", "keyspace_ai") \
                  .option("table", "table_ai") \
                  .mode("append") \
                  .save()) \
    .outputMode("update") \
    .start()

query.awaitTermination()
