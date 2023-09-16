def PeakElement(arr, n):
    if n == 1:
        return 0

    if arr[0] >= arr[1]:
        return 0

    if arr[n - 1] >= arr[n - 2]:
        return n - 1
    for i in range(n - 1):
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
            return i


if __name__ == '__main__':
    arr = [1, 3, 20, 200, 0]
    n = len(arr)
    print("The peak element index is:")
    result = PeakElement(arr, n)
    print(result)
