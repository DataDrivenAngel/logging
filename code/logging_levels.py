import logging

logging.basicConfig(format='%(asctime)s %(message)s',filename='basic_logging.log', level=logging.INFO)

message = "I don't always debug, but when I do, I use the standard logging module"

logging.info(message)