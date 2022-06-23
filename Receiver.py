import pika,os

def receptor():
	url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost:5672/")
	params = pika.URLParameters(url)
	connection = pika.BlockingConnection(params)
	channel = connection.channel()

	#channel.queue_declare(queue="mna29")

	def retrieveMessage(ch,method,properties,body):
		print("Message received %r" % body.decode())
		channel.basic_ack(method.delivery_tag)

	channel.basic_consume(queue="mna29", on_message_callback=retrieveMessage)
	channel.start_consuming()


receptor()