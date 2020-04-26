ID = input("Enter your mail id: ")
ID = list(ID)
st = ID.index("@")
end = ID.index(".", st)
i = st + 1
while st < i < end:
    print(ID[i], end="")
    i += 1
print("\n")
