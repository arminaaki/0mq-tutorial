import zmq
import os
import json
import logging

logging.basicConfig(level=int(os.environ['LOG_LEVEL']), format='[%(levelname)s] - %(asctime)s - (%(module)s) %(message)s')

logging.debug("Setting context for receive --> PULL")
receive_context = zmq.Context()
receive_socket  = receive_context.socket(zmq.PULL)
logging.debug("connecting %s" % os.environ['SERVER_HOSTNAME'])
receive_socket.connect(os.environ['SERVER_HOSTNAME'])

while True:
    logging.info("Waiting for the delivery")
    delivery = receive_socket.recv_json()
    logging.info("Received: %s" % delivery)
