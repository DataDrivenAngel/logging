#Basic logging in python

message = "I don't always debug, but when I do, I use print statements"

# "log" to console
print(message)

# enter the standard logging module
import logging
logging.warning(message)
