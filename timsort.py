import time
import matplotlib.pyplot as plt

MIN_MERGE = 32
SET_1 = 100000
SET_2 = 250000
SET_3 = 500000

def calc_min_run(n):
    """Calculate the minimum run length for TimSort."""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_part = arr[left:left + len1]
    right_part = arr[mid + 1:mid + 1 + len2]
    i, j, k = 0, 0, left
    
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)
    
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

def generate_ascending(set_size):
    return list(range(set_size + 1))

def generate_descending(set_size):
    return list(range(set_size, -1, -1))

def generate_random(set_size):
    if set_size == SET_1:
        filename = "set1.txt"
    elif set_size == SET_2:
        filename = "set2.txt"
    elif set_size == SET_3:
        filename = "set3.txt"
    else:
        raise ValueError("Tamanho de conjunto inválido")
    
    with open(filename, 'r') as f:
        arr = [int(line.strip()) for line in f]
    return arr

generators = [generate_ascending, generate_descending, generate_random]
generator_names = ["Crescente", "Decrescente", "Aleatório"]

def measure_time(arr):
    start = time.perf_counter()
    tim_sort(arr)
    end = time.perf_counter()
    return end - start

def apply_sets(generator_func):
    times = []
    for set_size in [SET_1, SET_2, SET_3]:
        dataset = generator_func(set_size)
        elapsed_time = measure_time(dataset)
        times.append(elapsed_time)
    return times

def apply_generators():
    all_times = []
    for i in range(3):
        print(f"\nTipo de função - {generator_names[i]}.")
        times = apply_sets(generators[i])
        all_times.append(times)
        for j, elapsed_time in enumerate(times, start=1):
            print(f"{elapsed_time:5.3f} - {j}° conjunto")
    return all_times

all_times = apply_generators()

set_sizes = [SET_1, SET_2, SET_3]
for i, times in enumerate(all_times):
    plt.plot(set_sizes, times, label=generator_names[i])

plt.xlabel("Tamanho do conjunto")
plt.ylabel("Tempo de execução (s)")
plt.title("Desempenho do TimSort")
plt.legend()
plt.grid()
plt.show()