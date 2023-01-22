def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr

if __name__ == '__main__':
    arr = [8, 5, 3, 10, 2, 1]
    print(bubble_sort(arr))
