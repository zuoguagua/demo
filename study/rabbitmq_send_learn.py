#!/usr/bin/env python

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare(queue="Hello")

message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange="",routing_key="Hello",body=message)

print "[X] Sent %r"%(message,)

connection.close()
