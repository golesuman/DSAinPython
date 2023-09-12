def valid_palindrome(input_string):
    i = 0
    j = len(input_string) - 1

    while i <= j:
        front = input_string[i]
        back = input_string[j]
        if front != back:
            return False
        i += 1
        j -= 1
    return True
    # pass


if __name__ == "__main__":
    tests = ['civic', 'radar', 'level', 'rotor', 'kayak', 'madam',  'refer']
    for test in tests:
        print(valid_palindrome(test))
