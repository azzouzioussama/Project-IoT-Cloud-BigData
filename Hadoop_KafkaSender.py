from kafka import KafkaProducer
from hdfs import InsecureClient
import json

# Kafka configuration
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# HDFS client
client = InsecureClient('http://192.168.44.129:9870', user='hadoop')

# Path to your HDFS directory containing CSV files
hdfs_path = '/data/'

# List all files in the specified HDFS directory
files = client.list(hdfs_path)

for file in files:
    # Assuming CSV files, read content. Adjust reading mechanism based on your data format.
    with client.read(hdfs_path + file, encoding='utf-8') as reader:
        csv_content = reader.read()
        # Here you should process your CSV file to extract or transform the data as needed

        # Send the data to Kafka
        producer.send('topic_sentimentPred', {'file': file, 'content': csv_content})
        print(f"Sent data from {file} to Kafka")

producer.close()
