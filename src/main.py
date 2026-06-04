import multiprocessing
import time
import math

LIMIT = 500000


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def sequential_prime():
    primes = []

    start = time.perf_counter()

    for i in range(LIMIT):
        if is_prime(i):
            primes.append(i)

    end = time.perf_counter()

    return len(primes), end - start


def worker(start_num, end_num):
    local_primes = []

    for i in range(start_num, end_num):
        if is_prime(i):
            local_primes.append(i)

    return local_primes


def parallel_prime():
    start = time.perf_counter()

    cpu_count = multiprocessing.cpu_count()

    chunk_size = LIMIT // cpu_count

    tasks = []

    for i in range(cpu_count):
        start_range = i * chunk_size

        if i == cpu_count - 1:
            end_range = LIMIT
        else:
            end_range = (i + 1) * chunk_size

        tasks.append((start_range, end_range))

    with multiprocessing.Pool(cpu_count) as pool:
        results = pool.starmap(worker, tasks)

    primes = []

    for result in results:
        primes.extend(result)

    end = time.perf_counter()

    return len(primes), end - start


if __name__ == "__main__":

    print("=" * 50)
    print("PARALLEL PRIME NUMBER CHECKER")
    print("=" * 50)

    total_seq, seq_time = sequential_prime()

    total_par, par_time = parallel_prime()

    speedup = seq_time / par_time

    print("\nRESULTS")
    print("-" * 50)

    print(f"Total Prime Numbers : {total_seq}")

    print(f"\nSequential Time : {seq_time:.4f} seconds")
    print(f"Parallel Time   : {par_time:.4f} seconds")

    print(f"\nSpeedup : {speedup:.2f}x")

    if speedup > 1:
        print("Parallel execution is faster.")
    else:
        print("Parallel execution is slower.")