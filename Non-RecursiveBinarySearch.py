def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example
arr = [10, 20, 30, 40, 50]
print(binary_search_iterative(arr, 40))