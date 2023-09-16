from multiprocessing import cpu_count


def frequencyofGivenNumber(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count


arr = [1, 1, 1, 2, 31]
n = len(arr)
key = 31
result = frequencyofGivenNumber(arr, n, key)
print(result)
