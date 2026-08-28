from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returns {result}")
        return result
    return wrapper

@logged
def add(a, b):
    return a + b

result = add(2, 3)
# Calling add with args=(2, 3), kwargs={}
# add returns 5
print(result) # 5