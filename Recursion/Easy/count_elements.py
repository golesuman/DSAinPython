def count_arr(arr):
    if len(arr) == 0:
        return 0

    return 1 + count_arr(arr[1:])


print(count_arr([1, 2, 3, 4]))
