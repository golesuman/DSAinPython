def geometricSum(n):
    if n == 0:
        return 1

    return 1 / pow(2, n) + geometricSum(n - 1)


if __name__ == '__main__':
    n = 4
    print(geometricSum(n))
