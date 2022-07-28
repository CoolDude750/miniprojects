import logging
logging.basicConfig(filename="test.log",level = logging.INFO)
logging.info("this is my first line of code")
logging.warning("this is the warm message")
logging.error("this is a error msg")
logging.c
l = [1,3,3,5,2,5,67,8,3,2,8,9]
for i in l:
    if i == 2:
        logging.info(i)
        logging.warning("warning found for user 2")

logging.shutdown()