def reverseArray(arr, n):
    start = 0
    end = n - 1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

    return arr


arr = [1, 2, 3, 4, 5]
result = reverseArray(arr, len(arr))
print(result)
