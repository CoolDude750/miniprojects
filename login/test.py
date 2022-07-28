import logging
logging.basicConfig(filename="test1.log" ,level = logging.INFO)
logging.info("this is first login file")
l = [1,2,3,4,5,6,7,7]
for i in l:
    if i == 2:
        logging.info(l)