def kthGreatestElement(arr, n, k):
    arr.sort()
    last = n - 1
    return arr[last - k + 1]


arr = [1, 2, 10, 3, 55, 23, 103]
n = len(arr)
k = 1
result = kthGreatestElement(arr, n, k)
print(result)
