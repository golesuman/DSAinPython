def MoveNegatives(arr, n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr


a = [-1, 3, 5, -12, 10]
n = len(a)
result = MoveNegatives(a, n)
print(result)
