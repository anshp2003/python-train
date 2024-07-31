from functools import wraps
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            results=[]
            for _ in range(n):
                result=func(*args,**kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(5)
def show(name):
    return f"hello {name}"
    

ob=show("ansh")
for i in ob:
    print(i)

from functools import wraps

def repeater(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            # Print the results after all repetitions
            print(f"Final result of function '{func.__name__}' repeated {n} ")
            return results
        return wrapper
    return decorator

# Function to perform addition
@repeater(5)
def add(x, y):
    return x + y

# Calling the decorated function
results = add(10, 20)
for i in results:
    print(i)




