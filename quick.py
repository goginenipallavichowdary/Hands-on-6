import random
import time
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def benchmark(input_arrays):
    execution_times = []
    for arr in input_arrays:
        start = time.time()
        quicksort(arr)
        end = time.time()
        execution_times.append(end - start)
    return execution_times

# Defining maximum input size and array sizes
max_size = 200
sizes = list(range(1, max_size + 1))

# Generating inputs for best, worst, and average cases
best_case = [list(range(1, size + 1)) for size in sizes]   # Best case: sorted arrays
worst_case = [list(range(size, 0, -1)) for size in sizes]  # Worst case: reverse sorted
average_case = [random.sample(range(1, size + 1), size) for size in sizes]  # Average case: random arrays

# Plotting the benchmark results
plt.plot(sizes, measure_time(sorted_inputs), label='Best Case')
plt.plot(sizes, measure_time(reverse_inputs), label='Worst Case')
plt.plot(sizes, measure_time(random_inputs), label='Average Case')

# Graph labels and legend
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Quicksort Benchmark with Fixed Pivot')
plt.legend()
plt.show()
