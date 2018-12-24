import zmq
import random
import sys
import time
import os

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect(os.environ['HOSTNAME'])

while True:
    socket.send("Client: Sending hi")
    msg = socket.recv()
    print("Client received: %s" % msg)
    time.sleep(5)
