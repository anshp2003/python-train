import time

def log_execution_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        execution_time=end_time-start_time
        print(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def show_time():
    for _ in range(1000000):
        pass

show_time() 