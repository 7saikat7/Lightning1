l = []
n = input().split(" ")
for items in range(len(n)):
    c=int(n[items])
    l.append(c)
j = list(dict.fromkeys(l))
for x in j:
    print(x, end=" ")
