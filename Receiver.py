import pika

def receptor():
	connect = pika.BlockingConnection(pika.ConnectionParameters(host='locahost'))
	channel = connection.channel()

	channel.queue_declare(queue="mna29")

	def callback(ch,method,properties,body):
		print("Message received %r" % body.decode())

	channel.basic_consume(queue="mna", on_message_callback=callback)
	channel.start_consuming()

report()