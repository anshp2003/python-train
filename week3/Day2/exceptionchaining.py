class FileProcessingError(Exception):
    pass

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileProcessingError("Error processing the file") from e

def process_data( filename):
    try:
        data = read_file(filename)
        # Further processing
    except FileProcessingError as e:
        print(f"An error occurred: {e}")
        print(f"Original exception: {e.__cause__}")

# Usage
try:
    process_data('non_existent_file.txt')
except FileProcessingError as e:
    print(f"Final error: {e}")
    print(f"Original cause: {e.__cause__}")
