numbers = input("Enter the numbers: ").split(",")
input_list = []
for n in numbers:
    k = int(n)
    input_list.append(k)
c = 50
h = 30
results = []
for d in input_list:
    z = 2 * c * d
    z = z / h
    Q = z ** 0.5
    results.append(Q)
i=0
while i< len(results):
    print(round(results[i]), end="")
    if len(results)-i==1:
        print("", end="")
    else:
        print(",", end="")
    i+=1
