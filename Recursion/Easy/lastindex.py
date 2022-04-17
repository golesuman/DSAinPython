def lastIndex(arr,x,si):
    n = len(arr)
    if si == n:
        return -1

    smallerListOutput = lastIndex(arr,x,si+1)
    if smallerListOutput != -1:
        return smallerListOutput

    else:
        if arr[si] == x:
            return si
        else:
            return -1

if __name__ == '__main__':
    arr = [1,5,3,5,7,9]
    print(lastIndex(arr,5,0))