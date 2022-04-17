def factorial(n):
    if n < 2:
        return n

    return n * factorial(n-1)


if __name__ == '__main__':
    result = factorial(5)
    print(result)