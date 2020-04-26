cons = input("Enter two numbers").split(",")
x = int(cons[0])
y = int(cons[1])
number_list = []
i = x
while i <= y:
    if i % 2 == 0:
        number_list.append(i)
    i += 1


def evenodd(a):
    even = 0
    odd = 0
    while a > 0:
        rem = a % 10
        if rem % 2 == 0:
            even += 1
        else:
            odd += 1
        a = int(a / 10)
    if odd >= 1:
        return 1
    else:
        return 0


i = 0
while i < len(number_list):
    k = evenodd(number_list[i])
    if k == 0:
        print(number_list[i], end="")
        if len(number_list) - i != 1:
            print(",", end="")
        else:
            print("", end="")
    i += 1
