import pika

connect = pika.BlockingConnection(pika.ConnectionParameters(host='locahost'))
channel = connect.channel()

channel.queue_declare(queue="mna29")

x = 1
while x < 5:
	msg=input("Enter your message: ")
	channel.basic_publish(exchange='', routing_key='mna29', body=msg)
	print("sent :", msg)
	x += 1

connect.close()