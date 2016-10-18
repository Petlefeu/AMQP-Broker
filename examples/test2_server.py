#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Example of an AMPQ Broker server """

# VERSION 1.3.0

import amqp_broker

def world_destroyer(string):
    """ This is an example function """
    return string.replace('World', 'Hell')

if __name__ == "__main__":
    BROKER_SERVER = amqp_broker.Server(world_destroyer, server_host='127.0.0.1')
    BROKER_SERVER.init()
