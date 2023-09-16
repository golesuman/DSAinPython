def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    for _ in range(len(arr) // 2):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 19
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
