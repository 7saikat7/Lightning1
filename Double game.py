import string
import random

symbols = list(string.ascii_letters)  # list of all alphabets
card1 = [0] * 5  # have 5 array elements of "0" value
card2 = [0] * 5
pos1 = random.randint(0, 4)  # if the range is given (0,5) it can also generate 5 then the list will be out of range
# so we generate 0 to 4.
pos2 = random.randint(0, 4)
# pos1 and pos2 are same card positions on two seperate cards that are to be compared
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)  # removes the letter from the list symbols.
if pos1 == pos2:
    card2[pos1] = samesymbol
    card1[pos1] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i = 0
while i < 5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1
print(card1)
print(card2)
ch = input("Spot the same letter: ")
if ch == samesymbol:
    print("Right")
else:
    print("Wrong")
