import pika 
connection = pika.BlockingConnection(pika.ConnectionParameters(host="13.77.169.144",credentials=pika.credentials.PlainCredentials("akshay","akshay")))
channel = connection.channel()
channel.queue_declare(queue = "hello");
channel.basic_publish(exchange='',routing_key='hello',body="hello world")

print("[x] send hello world")

connection.close()