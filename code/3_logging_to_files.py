import logging

logging.basicConfig(format='%(asctime)s %(levelname)s  %(message)s',filename='basic_logging.log', level=logging.INFO)

message = "I don't always log, but when I do I log to file"

logging.info(message)