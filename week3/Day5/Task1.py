import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug('this is debug message')
logging.info("this is an info message")
logging.warning("this is an warning")
logging.error("this is an error message")
logging.critical("this is a critical")