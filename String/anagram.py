from pyparsing import WordEnd


def anagram(word1, word2):
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word1 == word2:
        return True
    return False

if __name__ == '__main__':
    t = input('')
    s= input('')
    result= anagram(t,s)
    print(result)