from tqdm import tqdm

import logging
import logging.handlers

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# Create a logging handler to handle the log rotation
handler = logging.handlers.RotatingFileHandler(
              "rotating_log.log", maxBytes=2000, backupCount=5)

# Format the messages
handler.setFormatter(logging.Formatter('{asctime} {levelname} {message}', style= '{'))


# Add handler to the logger
logger.addHandler(handler)

message = "I don't always log, but when I do, I use log rotation"

# Log 100 entries
for i in tqdm(range(10000)):
    logger.info(message)

