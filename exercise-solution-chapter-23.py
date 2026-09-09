import time
from concurrent.futures import ProcessPoolExecutor

def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    sizes = [2_000_000, 3_000_000, 4_000_000, 5_000_000]

    start = time.perf_counter()
    sequential = list(map(sum_of_squares, sizes))
    sequential_time = time.perf_counter() - start

    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        parallel = list(executor.map(sum_of_squares, sizes))
    parallel_time = time.perf_counter() - start

    print(f"Sequential: {sequential_time:.2f}s") # Sequential: 0.50s
    print(f"Parallel: {parallel_time:.2f}s") # Parallel: 0.27s
    assert sequential == parallel  # same result, guaranteed by purity
    print("Results match")
