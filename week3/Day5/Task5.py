import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def add_items_to_list(items):
    """
    Adds items to a list and logs each operation.
    
    Parameters:
    - items (list): A list of items to be added.
    """
    my_list = []
    logging.info("Starting to add items to the list.")
    
    for item in items:
        try:
            logging.debug(f"Attempting to add item: {item}")
            if not isinstance(item, str):
                raise TypeError("Only strings can be added to the list.")
            my_list.append(item)
            logging.debug(f"Item added: {item}")
        except TypeError as e:
            logging.error(f"Error adding item {item}: {e}")
    
    logging.info(f"Final list: {my_list}")

# Example usage
items_to_add = ["apple", "banana", 42, "cherry"]
add_items_to_list(items_to_add)
