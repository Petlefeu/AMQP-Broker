#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Example of an AMPQ Broker server """

# VERSION 1.3.0

import amqp_broker

def example_func(parameter):
    """ This is an example function """
    try:
        var = int(parameter)
        result = var * var
    except ValueError:
        result = 'Nan'
    return result

if __name__ == "__main__":
    BROKER_SERVER = amqp_broker.Server(example_func, server_host='127.0.0.1')
    BROKER_SERVER.init()
