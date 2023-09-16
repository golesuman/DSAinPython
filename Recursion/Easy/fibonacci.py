from pickletools import read_uint1


def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    result = fibonacci(6)
    print(result)
