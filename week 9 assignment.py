l = []
n = input("Enter the number").split(" ")
for numbers in n:
    l.append(numbers)
l.sort()
x = 2
i = 0
if (l[0] != "1"):
    print("1")
else:
    while i < len(l) - 1:
        if int(l[i + 1]) - int(l[i]) != 1:
            print("missing= ", x)
        x += 1
        i += 1
