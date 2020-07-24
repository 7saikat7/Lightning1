def search(x, t):
    for j in range(0, len(t)):
        if t[j] == x:
            return j
    return -1


arr = []
for i in range(1, 10):
    arr.append(((i ** 2) - 4 * i / (2 * i)))
print(arr)
k = float(input("Enter the number you want to find"))
print(search(k, arr))
