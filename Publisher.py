import pika,os

url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost:5672/")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="mna29")

x = 1
while x < 5:
	msg=input("Enter your message: ")
	channel.basic_publish(exchange='', routing_key='mna29', body=msg)
	print("sent :", msg)
	x += 1

connection.close()