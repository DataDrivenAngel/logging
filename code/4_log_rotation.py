from tqdm import tqdm

import logging
import logging.handlers

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

#create a logging handler to handle the log rotation
handler = logging.handlers.RotatingFileHandler(
              "rotating_log.log", maxBytes=2000, backupCount=5)

handler.setFormatter('%(asctime)s %(levelname)s  %(message)s')
#add handler to the logger
logger.addHandler(handler)

message = "I don't always log, but when I do, I use log rotation"

for i in tqdm(range(100)):
    logger.info(message)

