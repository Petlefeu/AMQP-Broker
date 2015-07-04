#!/usr/bin/env python

# VERSION 1.1.0

import amqp_broker

def g(n):
    return n*n

broker_server = amqp_broker.Server(g, server_host='127.0.0.1')
broker_server.init()
