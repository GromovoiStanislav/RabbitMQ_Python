import os

import pika
from dotenv import load_dotenv

load_dotenv()

AMQP_LOGIN = os.environ.get('AMQP_LOGIN')
AMQP_PASSWORD = os.environ.get('AMQP_PASSWORD')
AMQP_HOST = os.environ.get('AMQP_HOST')
AMQP_VIRTUAL_HOST = os.environ.get('AMQP_VIRTUAL_HOST')
AMQP_PORT = os.environ.get('AMQP_PORT')

credentials = pika.PlainCredentials(username=AMQP_LOGIN, password=AMQP_PASSWORD)
parameters = pika.ConnectionParameters(host=AMQP_HOST, virtual_host=AMQP_VIRTUAL_HOST, credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):
    print(str(body.decode('utf-8')))

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()