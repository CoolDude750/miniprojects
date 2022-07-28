import logging
logging.basicConfig(filename="test3.log",level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s' )

logging.warning("this is the warm message")
logging.error("this is a error msg")
def divide(a,b):
    logging.info("The number entered by user is %s and %s" , a,b)
    try :
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation ")
        logging.info("the result is %s ", div)
        return div
    except Exception as e :
        logging.exception(e)

print((divide(3,6)))