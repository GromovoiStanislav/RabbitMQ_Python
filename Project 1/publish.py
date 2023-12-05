import datetime
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
parameters = pika.ConnectionParameters(host=AMQP_HOST, virtual_host=AMQP_VIRTUAL_HOST, port=AMQP_PORT,credentials=credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

s = datetime.datetime.now()
for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello, World! ' + str(datetime.datetime.now()))
# print(" [x] Sent 'Hello, World!'")
print((datetime.datetime.now() - s).total_seconds())

connection.close()
