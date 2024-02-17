#%%
import random
import time

from InsertionSort import insertion_sort
from MergeSort import merge_sort
from TimSort import tim_sort

SEED  = 765
DATA_SIZE = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

insertion_sort_counts = []
merge_sort_counts = []
tim_sort_counts = []

insertion_sort_time = []
merge_sort_time = []
tim_sort_time = []

def generate_random_array(n):
    random.seed(SEED)
    return [random.randint(1, 1000) for _ in range(n)]

for size in DATA_SIZE:
    input = generate_random_array(size)

    start_time  = time.time()
    insertion_sort_counts.append(insertion_sort(input[:]))
    insertion_sort_time.append(round(time.time() - start_time, 8)*1000)

    start_time  = time.time()
    merge_sort_counts.append(merge_sort(input[:]))
    merge_sort_time.append(round(time.time() - start_time, 8)*1000)

    start_time  = time.time()
    tim_sort_counts.append(tim_sort(input[:]))
    tim_sort_time.append(round(time.time() - start_time, 8)*1000)


print(f'insertion_sort_counts = {insertion_sort_counts}')
print(f'merge_sort_counts = {merge_sort_counts}')
print(f'tim_sort_counts = {tim_sort_counts}')

print(f'insertion_sort_time = {insertion_sort_time}')
print(f'merge_sort_time = {merge_sort_time}')
print(f'tim_sort_time = {tim_sort_time}')

#%%
# Plotting the time complexity graph w.r.t comparision & swap counts.
import matplotlib.pyplot as plt
plt.plot(DATA_SIZE, insertion_sort_counts, label='Insertion Sort')
plt.plot(DATA_SIZE, merge_sort_counts, label='Merge Sort')
plt.plot(DATA_SIZE, tim_sort_counts, label='Tim Sort')
plt.xlabel('Array Size')
plt.ylabel('Count')
plt.title('Time Complexity of Sorting Algorithms w.r.t COUNTS')
plt.legend()
plt.grid(True)
plt.show()

#%%
# Plotting the time complexity graph w.r.t execution time.
import matplotlib.pyplot as plt
plt.plot(DATA_SIZE, insertion_sort_time, label='Insertion Sort')
plt.plot(DATA_SIZE, merge_sort_time, label='Merge Sort')
plt.plot(DATA_SIZE, tim_sort_time, label='Tim Sort')
plt.xlabel('Array Size')
plt.ylabel('Time(ms)')
plt.title('Time Complexity of Sorting Algorithms w.r.t EXECUTION TIME')
plt.legend()
plt.grid(True)
plt.show()
    


