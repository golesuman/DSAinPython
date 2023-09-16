def two_sum_array_is_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        if total > target:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    arr = [2, 7, 12, 15, 19, 20, 23]
    target = 38

    result = two_sum_array_is_sorted(arr, target)
    print(result)
