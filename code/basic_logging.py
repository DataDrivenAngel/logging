
# 
message = "I don't always debug, but when I do, I use print statements"
message = "Request returned HTTP 200"
print(message)

import logging

logging.basicConfig(format='%(asctime)s %(message)s',filename='basic_logging.log', level=logging.INFO)
logging.info(message)
