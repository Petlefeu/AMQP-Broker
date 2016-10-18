#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Example of an AMPQ Broker client """

# VERSION 1.3.0

import amqp_broker

BROKER_CLIENT = amqp_broker.Client(server_host='127.0.0.1')

print " [.] %s" % BROKER_CLIENT.send('HelloWorld')
