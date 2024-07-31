# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         # Log the function call with its arguments
#         print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        
#         # Call the original function and store its result
#         result = func(*args, **kwargs)
        
#         # Log the result of the function call
#         print(f"Function '{func.__name__}' returned {result}")
        
#         # Return the result
#         return result
    
#     return wrapper

# @log_decorator
# def add(a, b):
#     return a + b

# @log_decorator
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# # Call the decorated functions
# add(3, 5)
# greet("Alice")
# greet("Bob", greeting="Hi")


import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def slow_function():
    # time.sleep(5)
    print("Function complete.")

slow_function()


def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('permission') == permission:
                return func(user, *args, **kwargs)
            else:
                print(f"User {user['name']} does not have {permission} permission.")
        return wrapper
    return decorator

@requires_permission('admin')
def access_admin_panel(user):
    print(f"Welcome {user['name']} to the admin panel.")

user = {'name': 'Alice', 'permission': 'admin'}
access_admin_panel(user)  # This will allow access

user = {'name': 'Bob', 'permission': 'user'}
access_admin_panel(user)  # This will deny access



