from re import sub


def countSubstring(string,substring):
    string = list(string)
    substring = list(substring)
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

if __name__ == '__main__':
    c = countSubstring('haripacpacpac','pac')
    print(c)