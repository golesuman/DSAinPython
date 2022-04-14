def findingDuplicates(arr,size):
    arr.sort()
    for i in range(size):
        if arr[i] == arr[i+1]:
            return arr[i]

if __name__ == '__main__':
    print("Enter the size of an array:")
    size = int(input())
    print("Enter the elements of an array")
    arr = []
    for i in range(size):
        ele = int(input())
        arr.append(ele)

    result = findingDuplicates(arr, size)
    print(f'The duplicate element is {result}')
        