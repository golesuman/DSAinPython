def findDuplicate(array, size):
    array.sort()
    for i in range(size):
        if array[i] == array[i + 1]:
            return array[i]


if __name__ == "__main__":
    array = [1, 3, 5, 3, 2]
    size = len(array)
    result = findDuplicate(array, size)
    print(result)
