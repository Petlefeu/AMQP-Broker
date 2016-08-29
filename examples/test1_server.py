#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Example of an AMPQ Broker server """

# VERSION 1.1.1

import amqp_broker

def example_func(parameter):
    """ This is an example function """
    return parameter * parameter

if __name__ == "__main__":
    BROKER_SERVER = amqp_broker.Server(example_func, server_host='127.0.0.1')
    BROKER_SERVER.init()
