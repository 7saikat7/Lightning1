x = input("Enter the words: ").split(",")
word_list = []
for words in x:
    word_list.append(words)
word_list.sort()
i = 0
while i < len(word_list):
    print(word_list[i], end="")
    if len(word_list) - i == 1:
        print("", end="")
    else:
        print(",", end="")
    i += 1
