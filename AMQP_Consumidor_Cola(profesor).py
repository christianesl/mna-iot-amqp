import pika,os

def receptor():
    url = os.environ.get('CLOUDAMQP_URL', 'pon aquí la dirección de tu server')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    #ahora declaramos la cola o queue que vamos a 'consumir'
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print("Mensaje recibido %r" % body.decode())

    channel.basic_consume(queue="hello",on_message_callback=callback)
    channel.start_consuming()

receptor()
