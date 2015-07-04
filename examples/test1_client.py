#!/usr/bin/env python

# VERSION 1.1.0

import amqp_broker

broker_client = amqp_broker.Client(server_host='127.0.0.1')

print " [.] %s" % broker_client.send(10)
