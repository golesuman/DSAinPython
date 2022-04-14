def PeakElement(arr, n):
    maxI = 0
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            maxI = i
    return maxI

if __name__ == '__main__':
    arr = [10,20,30,89,0,1,8,99,108,90,5,2]
    n = len(arr)
    result = PeakElement(arr,n)
    print(result)        

