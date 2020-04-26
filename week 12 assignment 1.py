p=int(input("Enter the number of lines:  "))
sentenses=[]
for i  in range(p):
    sentenses.append(input("enter youur sentence"))
for i in range (p):
    print(sentenses[i].upper(),"\n")