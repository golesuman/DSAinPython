def sumofNatural(n):
    if n == 0:
        return n

    return n + sumofNatural(n-1)

if __name__ == '__main__':
    result = sumofNatural(5)
    print(result)