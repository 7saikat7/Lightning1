a = []
n = input("Enter the number").split(" ")
for numbers in n:
    numbers = int(numbers)
    a.append(numbers)
a.sort()
i = 1
for k in a:
    if k < 0:
        print(k, end=" ")
    elif k > 0:
        if k != i:
            print("-1", end=" ")
            print(i + 1, end=" ")
            i = k
        elif k == i:
            print(k, end=" ")
        else:
            print(k, end=" ")
        i += 1
