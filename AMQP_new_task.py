#!/usr/bin/env python
import pika as pika
import os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://ekrrafvx:6DZsd-zG_NvZqZDbrQDIlhR0MKV8b3uP@gull.rmq.cloudamqp.com/ekrrafvx')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='IoT', durable=True)

#message = ' '.join(sys.argv[1:]) or "Rigo!"
message = input("Que quieres mandar: ")
channel.basic_publish(
    exchange='',
    routing_key='IoT',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

print(" [x] Sent %r" % message)
connection.close()


