import time
from functools import cache

@cache
def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

def count_ways_sin_memo(n):
    if n <= 1:
        return 1
    return count_ways_sin_memo(n - 1) + count_ways_sin_memo(n - 2)

inicio = time.perf_counter()
print(count_ways_sin_memo(30)) # 1346269
print(f"{time.perf_counter() - inicio:.4f}s") # 0.1506s

inicio = time.perf_counter()
print(count_ways(30)) # 1346269
print(f"{time.perf_counter() - inicio:.6f}s") # 0.000034s