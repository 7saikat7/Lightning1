z = open("file.txt", 'a+')
with open("file.txt", 'r') as f:
    for lines in f:
        print("lines:-\t", lines)  # file is already arranged into lines by default
        for word in lines:
            words = word.split()  # sentences splitted into words
            # print('words:-\t', words)
            if words == ['b'] or words == ['B']:
                print(['CHANGED'])
            else:
                print(words)
z.close()
