import logging

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# logging.debug('this is debug message')
# logging.info("this is an info message")
# logging.warning("this is an warning")
# logging.error("this is an error message")
# logging.critical("this is a critical")




# logging.basicConfig(filename="Test.log" ,level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# logging.debug('this is debug message')
# logging.info("this is an info message")
# logging.warning("this is an warning")
# logging.error("this is an error message")
# logging.critical("this is a critical")



# logging.basicConfig(filename="Test.log" ,level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# def divide(a,b):
#     try:
#         result=a/b
#         logging.info(f"Dividing {a} {b} gives {result}")
#     except ZeroDivisionError:
#         logging.exception('attemted to divide by zero')
#         return None


# divide(10,2)
# divide(10,0)        


import logging

# Set up basic configuration for logging to a file
logging.basicConfig(filename='Test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(a, b):
    try:
        result = a / b
        logging.info(f'Dividing {a} by {b} gives {result}')
        return result
    except ZeroDivisionError:
        logging.exception('Attempted to divide by zero')
        return None

# Log messages of varying severity
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Using the divide function
divide(10, 2)
divide(10, 0)
