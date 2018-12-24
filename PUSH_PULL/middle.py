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

logging.debug("Setting context for receive --> PUSH")
send_context = zmq.Context()
send_socket = send_context.socket(zmq.PUSH)
send_socket.bind(os.environ['SELF_HOSTNAME'])

while True:
    logging.debug("Waiting for the server to send my pizza")
    pizza = receive_socket.recv_json()
    logging.debug("Received : %s" % pizza)
    
    send_socket.send_json(pizza)
    logging.debug("Data sent to the client")


