#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# VERSION 1.1.0

import pika
import uuid

class Client(object):
    def __init__(self, server_host='127.0.0.1', key='hello'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=server_host))
        self.key = key
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def send(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.key,
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

class Server(object):
    def __init__(self, func, server_host='127.0.0.1', key='hello'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters( 
            host=server_host ))
        self.key = key
        self.func = func
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.key)

    def on_request(self, ch, method, props, body):
        # TODO
        # More tweakable.
        n = int(body)

        print " [.] f(%s)"  % (n,)
        response = self.func(n)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                            correlation_id = props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def init(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request, queue=self.key)

        print " [x] Démarrage du serveur."
        self.channel.start_consuming()
