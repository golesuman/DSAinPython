def firstIndex(a,x):
    n = len(a)
    if n == 0:
        return -1
    if a[0] == x:
        return 0

    smallerListOutput = firstIndex(a[1:],x)
    if smallerListOutput == -1:
        return -1

    else:
        return smallerListOutput + 1

def firstIndexB(a,x, si):
    l = len(a)
    if si == l:
        return -1
    if a[si] == x:
        return si

    smallerListOutput = firstIndexB(a,x,si+1)
    return smallerListOutput
if __name__ == '__main__':
    a = [1,2,3,5,7,9,7]
    print(firstIndex(a,7))
    print(firstIndexB(a,7,0))