#Basic logging in python

message = "I don't always debug, but when I do, I use print statements"

#tis
print(message)

import logging

logging.basicConfig(format='%(asctime)s %(message)s',filename='basic_logging.log', level=logging.INFO)
logging.info(message)
