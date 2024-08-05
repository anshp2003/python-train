# with open("demo.txt","r+") as obj:
#     print(obj.read())
#     obj.write("my name is karm \n")
#     print(obj.read())


from contextlib import contextmanager
from time import time

# @contextmanager
# def Timer():
#     start=time()
#     yield 88888*8*3
#     end=time()
#     print(f"took : {(end-start):.4f}s")

# with Timer() as a:
#     print(a)
#     for i in range(10000):
#         i*i*i


# @contextmanager
# def filename(filename,mode):
#     file1=open(filename,mode)
#     yield file1
#     file1.close()
# with filename("demo.txt","r")as file:
#     print(file.read())


class file1:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.file.close()        

with file1("demo.txt","r") as file:
    data=file.read()
    print(data)



class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect_to_database(self):
        print(f"Connecting to database {self.db_name}...")
        return f"Connection to {self.db_name}"

    def close_connection(self):
        print(f"Closing the connection to {self.db_name}...")
        self.connection = None
        
    def __enter__(self):
        self.connection = self.connect_to_database()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
        if exc_type is not None:
            print(f"Exception: {exc_val}")
        return True  # Suppress exceptions if handled


# Using the context manager
with DatabaseConnection('ansh_database') as connection:
    print(f"Using {connection}")
    # Perform database operations here
    # Uncomment the next line to simulate an exception
    # raise ValueError("Simulated error")
