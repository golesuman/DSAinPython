def two_sum_array_is_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] == target:
            return left, right
        left += 1
        right -= 1


if __name__ == "__main__":
    arr = [-1, 0]
    target = -1

    result = two_sum_array_is_sorted(arr, target)
    print(result)
