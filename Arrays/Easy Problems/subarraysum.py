def SubarraySum(arr, n, key):
    for i in range(n):
        currentSum = arr[i]
        j = i + 1
        while j <= n:
            if currentSum == key:
                print(f'The indices are {i} and {j - 1} ')

            if currentSum > key or j == n:
                break
            currentSum += arr[j]
            j += 1


arr = [1, 2, 7, 3, 5]
key = 8
SubarraySum(arr, len(arr), key)
