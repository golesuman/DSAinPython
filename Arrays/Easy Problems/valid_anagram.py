def is_anagram(s, t):
    count_char, count_char_t = {}, {}
    for char in s:
        count_char[char] = count_char.get(char, 0) + 1
    for char in t:
        count_char_t[char] = count_char_t.get(char, 0) + 1
    
    for key in count_char:
        if count_char[key] != count_char_t[key]:
            return False
    return True




if __name__ == '__main__':
    # s = input("Enter a string:")
    # t = input("Enter another string:")
    s = "start"
    t = "tarst"
    if is_anagram(s, t):
        print(f"{s} and {t} are anagrams")
    else:
        print(f"{s} and {t} are not anagrams")
    

