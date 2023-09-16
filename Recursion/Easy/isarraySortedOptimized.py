def isArraySorted(arr, start):
    n = len(arr)
    if start == n - 1 or start == n:
        return True
    if arr[start] > arr[start + 1]:
        return False

    return isArraySorted(arr, start + 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 40, 5]
    print(isArraySorted(arr, start=0))
