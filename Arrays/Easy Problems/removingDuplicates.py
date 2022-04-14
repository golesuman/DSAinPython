def removeDuplicates(arr):
    arrUnique = []
    for element in arr:
        if element not in arrUnique:
            arrUnique.append(element)

    return arrUnique


if __name__ == '__main__':
    print("Enter the size of an array")
    size = int(input())
    print("Enter the elements of an array:")
    i = 0 
    arr = []
    while i < size:
        ele = int(input())
        arr.append(ele)
        i += 1
    array = removeDuplicates(arr)
    print(array)