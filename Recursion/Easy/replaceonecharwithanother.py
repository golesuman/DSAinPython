from cgitb import small
from dataclasses import replace


def replaceChar(arr, a, b):
    if len(arr) == 0:
        return arr

    smallOutput = replaceChar(arr[1:] , a, b)

    if arr[0] == a:
        return b + smallOutput
    else:
        return arr[0] + smallOutput


if __name__ == '__main__':
    arr = 'arbapatiman'
    print(replaceChar(arr, 'a', 'b'))
