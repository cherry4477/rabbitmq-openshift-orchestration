#!/usr/bin/env python
import pika

parameters = pika.URLParameters('amqp://admin:test1234@localhost:5672/%2F')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()