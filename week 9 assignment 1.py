number = input("Enter the number: ")
x = 0
y = 0
for i in number:
    if i == "0":
        x += 1
    else:
        y += 1
if x == 1 or y == 1:
    print("YES")
    if x > y:
        for i in number:
            if i == "1":
                print("0", end="")
            else:
                print("0", end="")

    if y > x:
        for i in number:
            if i == "0":
                print("1", end="")
            else:
                print("1", end="")
else:
    print("NO")
