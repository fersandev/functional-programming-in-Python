import time
from functools import reduce

def timed(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

def sum_large_list(n):
    total = reduce(lambda accumulator, element: accumulator + element, range(n), 0)
    return total

timed_sum = timed(sum_large_list)
result = timed_sum(10_000_000) # Execution time: 4.310352 seconds
print(result) # 49999995000000
