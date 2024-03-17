import pika
import json
from hdfs import InsecureClient
import pandas as pd

# Initialize an empty list to hold the data
data = []

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange and queue, if needed
channel.exchange_declare(exchange='sentimentPred', exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='sentimentPred', queue=queue_name, routing_key='sentimentPred/test')

def callback(ch, method, properties, body):
    global data
    message = json.loads(body)
    data.append(message)
    print(f"Received message: {message}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Interrupted')
    # Optional: Add any cleanup here before exiting
    channel.stop_consuming()

connection.close()
print('Connection closed. Exiting.')

# Convert the accumulated data to a DataFrame and then to a CSV
df = pd.DataFrame(data)
csv_data = df.to_csv(index=False)

# Save the CSV to Hadoop HDFS
client = InsecureClient('http://192.168.44.129:9870', user='hadoop')
with client.write(hdfs_path = '/data/test.csv', encoding='utf-8') as writer:
    writer.write(csv_data)

print('CSV file saved to Hadoop HDFS.')
