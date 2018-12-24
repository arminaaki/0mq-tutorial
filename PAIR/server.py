import zmq
import os
import time

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind(os.environ['HOSTNAME'])
while True:
    socket.send("Server: Sending hello world")
    msg = socket.recv()
    print("Server received: %s" % msg)
    time.sleep(1)
