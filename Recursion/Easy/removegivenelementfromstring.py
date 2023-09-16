def removeGivenElement(arr, x):
    if len(arr) == 0:
        return arr

    if arr[0] == x:
        return removeGivenElement(arr[1:], x)

    return arr[0] + removeGivenElement(arr[1:], x)


if __name__ == '__main__':
    print(removeGivenElement('axbcxdxgxp', 'x'))
