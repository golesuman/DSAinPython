def counter(string):
    count = 1
    for i in range(len(string)):
        if string[i].isupper():
            count += 1

    return count


def main():
    c = counter('heySumanWhatAreYouDoing')
    print(c)


if __name__ == '__main__':
    main()
