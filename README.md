# AMQP-Broker

## AMQP Node/Cluster configuration

```bash
sudo apt-get install rabbitmq-server
```

Another way is to use **Docker** :

```bash
# Pulling docker image from repo
sudo docker pull bijukunjummen/rabbitmq-server

# Clone the github project and start the cluster
sudo git clone https://github.com/bijukunjummen/docker-rabbitmq-cluster
cd docker-rabbitmq-cluster/cluster
sudo docker-compose up -d
```

## AMQP Client configuration

```bash
sudo apt-get install python-pika
```

## VERSION

  - 1.3.2-1.3.1
    * Doc fix
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

## TODO

  - Make a real documentation
  - More examples and real use-case
  - Possibility to change every variables on every sides
  - Understanding every variables...

## SOURCES

https://www.rabbitmq.com/tutorials/tutorial-six-python.html
https://github.com/bijukunjummen/docker-rabbitmq-cluster