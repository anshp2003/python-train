import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def process_number(num):
    logging.info("starting the process")
    for i in num:
        logging.debug(f"processing number:{i}")
        r=i*2
        logging.debug(f"result after:{r}")
    logging.info('finish the process')
num=[0,10,20]
process_number(num)        
        