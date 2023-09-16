def PrintingNumbersAscending(n):
    if n == 0:
        return 0

    PrintingNumbersAscending(n - 1)
    print(n)


def PrintingNumberDescending(n):
    if n == 0:
        return 0
    print(n)
    PrintingNumberDescending(n - 1)


if __name__ == '__main__':
    PrintingNumbersAscending(5)
    print("Descending")
    PrintingNumberDescending(5)
