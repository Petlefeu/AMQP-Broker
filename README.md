## AMQP-Broker

# AMQP Node/Cluster configuration

<code bash>
sudo apt-get install rabbitmq-server
</code>

Another way is to use Docker :

<code bash>
sudo docker pull bijukunjummen/rabbitmq-server

sudo git clone https://github.com/bijukunjummen/docker-rabbitmq-cluster

cd docker-rabbitmq-cluster/cluster

sudo docker-compose up -d
</code>

# AMQP Client configuration

<code bash>
sudo apt-get install python-pika
</code>

# VERSION

  - 1.3.1
    * Doc issues
  - 1.3.0
    * New example added
    * English translation
    * Correction to the code (allowing string)
    * Add exception in test1 to cast string into integer
  - 1.2.0
    * Add authentication
  - 1.1.1
    * Documentation
    * Add more understanding errors
  - 1.1.0
    * Add configure.sh, can move the library to the python path
    * Change directories order
    * UTF-8 by default
  - 1.0.1
    * Add documentation
  - 1.0.0
    * Stable version of amqp-broker

# TODO

  - Make a real documentation
  - More examples and real use-case
  - Possibility to change every variables on every sides
  - Understanding every variables...

# SOURCES

https://www.rabbitmq.com/tutorials/tutorial-six-python.html
