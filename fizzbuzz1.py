for i in range(1, 51):
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    else:
        print(i)
