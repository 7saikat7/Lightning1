x = input("enter your sentence: ")
x = list(x)
print(x)
U = 0
L = 0
for i in x:
    if i.isalpha():
        if i.isupper():
            print(i, ":", end=" ")
            U += 1
            print(U)
        else:
            print(i, ":", end=" ")
            L += 1
            print(L)
print(U, " ", L)
