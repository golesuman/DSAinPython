def MinMax(a,n):
    minE = 0
    maxE = 0
    for i in range(n):
        if a[i] > maxE:
            maxE = a[i]

        if a[i] < minE:
            minE = a[i]

    return minE, maxE


if __name__ == '__main__':
    arr = [1,12,0,4,2]
    n = len(arr)
    result = MinMax(arr,n)
    print(result[0], result[1])