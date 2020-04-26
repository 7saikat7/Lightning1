total = int(input("Enter how many songs you have in your list: "))
i = 1
computing_paradox = []
print("enter the length of songs sperated by space: ")
n = input().replace(" ","")
#z = n.replace(" ", "")
k = int(n)
rem = 0
while i <= total:
    if not k == 0:
        rem = int(k % 10)

        computing_paradox.append(rem)
        k = k / 10
    i = i + 1
computing_paradox.reverse()
print("your given list: ", computing_paradox)
q = int(input("which song you want to find: "))
item = computing_paradox[q-1]
computing_paradox.sort()
print("sorted list: ",computing_paradox)
result = computing_paradox.index(item)
print("your song is in", result + 1, "index")
