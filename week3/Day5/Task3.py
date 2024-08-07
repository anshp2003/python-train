import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def number(num):
    logging.info("process start")
    for i in num:
        logging.debug(f"processing number {i}")
        if (i%2==0):
            logging.debug("sucess")
        else:
            logging.error("this number not divsible")
    logging.debug("process complete")

num=[0,4,5,8,7,10]
number(num)                



import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def log_messages(level, message):
    """
    Logs a message at the specified level.

    Parameters:
    - level (str): The log level ('debug', 'info', 'warning', 'error', 'critical').
    - message (str): The message to log.
    """
    if level == 'debug':
        logging.debug(message)
    elif level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
    else:
        logging.error("Invalid log level specified. Please use 'debug', 'info', 'warning', 'error', or 'critical'.")

# Example usage
log_messages('debug', 'This is a debug message.')
log_messages('info', 'This is an info message.')
log_messages('warning', 'This is a warning message.')
log_messages('error', 'This is an error message.')
log_messages('critical', 'This is a critical message.')
log_messages('unknown', 'This should show an error about invalid log level.')
