from string import ascii_lowercase as asl


def check(s):
    return set(asl) - set(s.lower()) == set([])


string = input("Enter string: ")
if check(string) == True:
    print("The string is panagram !")
else:
    print("The string isn't a panagram !")
