import time
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} completed")
        return result
    return wrapper

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIME] {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
