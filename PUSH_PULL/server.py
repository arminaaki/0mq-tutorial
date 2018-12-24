import zmq
import os
import json
import logging


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

logging.basicConfig(level=int(os.environ['LOG_LEVEL']), format='[%(levelname)s] - %(asctime)s - (%(module)s) %(message)s')

pizza = {
    "name": "pepperoni", 
    "sauce": "empty", 
    "topping": "empty"
}

context = zmq.Context()
socket = context.socket(zmq.PUSH)

logging.debug("binding to %s" % os.environ['SELF_HOSTNAME'])
socket.bind(os.environ['SELF_HOSTNAME'])

for id in range(1,100):
    delivery = merge_two_dicts({'id': id}, pizza)

    logging.debug("sending message %s" % delivery)
    socket.send_json(json.dumps(delivery))
