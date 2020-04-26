"""def vowel(c):
    return (c == "a") or (c == "e") or (c == "i") or (c == "o") or (c == "u")


def remove_vow(s):
    print(s[0], end="")
    for i in range(1, len(s)):
        if (vowel(s[i - 1]) != True) or (vowel(s[i] != True)):
            print(s[i], end="")
    return


string = input("enter string: ")
remove_vow(string)"""

def vowel(c):
    return (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u')

def remove_vow(s):
    print(s[0], end="")
    for i in range(1, len(s)):
        if (vowel(s[i - 1]) != True) or (vowel(s[i]) != True):
            print(s[i], end="")


string = input("Enter string: ")
remove_vow(string)
