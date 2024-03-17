import pika
import json
import pandas as pd

# Load the CSV file
df = pd.read_csv('data/test.csv')

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange, if needed
channel.exchange_declare(exchange='sentimentPred', exchange_type='topic')

# Sending each row as a JSON message
for _, row in df.iterrows():
    message = row.to_json()
    channel.basic_publish(exchange='sentimentPred', routing_key='sentimentPred/test', body=message)
    print(f"Sent message: {message}")

connection.close()
