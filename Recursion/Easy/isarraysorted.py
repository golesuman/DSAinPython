def isSorted(a):
    n = len(a)
    if n == 0 or n == 1:
        return True
    
    if a[0] > a[1]:
        return False

    return isSorted(a[1:])


if __name__ == '__main__':
    a = [1,2,3,9,5]
    print(isSorted(a))