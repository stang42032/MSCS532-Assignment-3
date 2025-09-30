import random

# ----------------------------
# 2-Way Randomized Quicksort
# ----------------------------

def randomized_quicksort(arr, low, high):
    """Sorts arr[low..high] in place using randomized Quicksort."""
    if low < high:
        # Partition the array around a random pivot
        pivot_index = random_partition(arr, low, high)
        # Recursively sort elements before and after partition
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def random_partition(arr, low, high):
    """Selects a random pivot and partitions the array."""
    pivot_index = random.randint(low, high)
    # Swap pivot with last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    """Standard 2-way partitioning around the pivot."""
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ----------------------------
# Test the algorithm
# ----------------------------

if __name__ == "__main__":
    # Generate a random array
    arr = [random.randint(1, 100) for _ in range(15)]
    print("Original array:")
    print(arr)

    # Run randomized Quicksort
    randomized_quicksort(arr, 0, len(arr) - 1)

    print("\nSorted array:")
    print(arr)
