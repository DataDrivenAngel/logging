# Logging has severity levels


# LEVEL    | VALUE
# CRITICAL | 50
# ERROR    | 40
# WARNING  | 30
# INFO     | 20
# DEBUG    | 10
# NOTSET   | 0


import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)


message = "I don't always debug, but when I do, I use the standard logging module"

logging.debug(message)
logging.info(message)
logging.warning(message)
logging.critical(message)