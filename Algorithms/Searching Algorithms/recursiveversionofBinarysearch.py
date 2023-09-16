def BinarySearch(arr, start, end, key):
    if start <= end:
        mid = start + (end - 1) // 2

        if arr[mid] == key:
            return mid

        elif key > arr[mid]:
            return BinarySearch(arr, mid + 1, end, key)


        else:
            return BinarySearch(arr, start, mid - 1, key)

    else:
        return -1


arr = [1, 3, 5, 7, 8]
key = 3

result = BinarySearch(arr, 0, len(arr) - 1, key)

if result != -1:
    print('Element is present at index %d' % result)

else:
    print('Element is not in an array')
