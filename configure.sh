#!/bin/bash

if ! dpkg -s python-pika >/dev/null 2>&1; then
    sudo apt-get install python-pika
fi

sudo cp amqp_broker.py /usr/lib/python2.7/

# sudo chmod +x /usr/local/bin/amqp_broker.py
