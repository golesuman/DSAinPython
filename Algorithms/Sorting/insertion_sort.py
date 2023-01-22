def insertion_sort(arr):
    for  i in range(len(arr)):
        j = i-1
        current = arr[i]
        while arr[j] > current and j >=0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1], current = current, arr[j+1]
    return arr

if __name__ == "__main__":
    arr = [8, 5, 3, 10, 2, 1]
    print(insertion_sort(arr))

        