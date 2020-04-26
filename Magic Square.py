print("Enter The number of rows in a magic Square")
n = int(input("The nmber should be odd: "))
"""def magic (n):
    square=[]
    for i in range (n):
        l=[]
        for j in range(n):
            l.append(0)
            square.append(l)
    # traditional way to create a matrix as shown above
    print("Printing traditional way!")
    for i in range(n):
        for j in range(n):
            print(square[i][j],end=" ")
        print()"""


def magic_Square(k):
    square = [[0 for i in range(k)] for j in range(k)]
    # modern way to create a matrix
    i = k // 2  # this is integer division which is equal to int(a/b)
    j = k - 1
    num = k * k
    c = 1  # this the matrix elements
    while c <= num:
        if i == -1 and j == k:
            j = k - 2
            i = 0
        else:
            if j == k:
                j = 0
            if i < 0:
                i = k - 1
        if square[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            square[i][j] = c
            c += 1
        i -= 1
        j += 1
    for a in range(k):
        for b in range(k):
            print(square[a][b], end=" ")
        print()
    return


magic_Square(n)

