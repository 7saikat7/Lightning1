import random


def play():
    pl1 = input("Enter player 1 name: ")
    pl2 = input("Enter player 2 name: ")
    ppl1 = 0
    ppl2 = 0
    turn = 0
    while True:
        picked_word = choose()
        qn = jumbled(picked_word)
        print(qn)
        # player1's  turn
        if turn % 2 == 0:
            print(pl1, "'s turn")
            ans = input("Your answer: ")
            if ans == picked_word:
                ppl1 += 2
                print(pl1, " score:", ppl1)
            else:
                ppl1 -= 1
                print(pl1, " score:", ppl1)
                print("The right answer is:", picked_word)
            print("Do you want to continue: ")
            print("Press 0 to continue 1 to quit: ")
            c = int(input("give your answer: "))
            if c == 1:
                thank(pl1, pl2, ppl1, ppl2)
                break
        # player2's turn
        else:
            print(pl2, "'s turn")
            ans = input("Your answer: ")
            if ans == picked_word:
                ppl2 += 2
                print(pl2, " score:", ppl2)
            else:
                ppl2 -= 1
                print(pl2, " score:", ppl2)
                print("The right answer is:", picked_word)
            print("Do you want to continue: ")
            print("Press 0 to continue 1 to quit: ")
            c = int(input("give your answer: "))
            if c == 1:
                thank(pl1, pl2, ppl1, ppl2)
                break
        turn += 1


def choose():
    words = ['computer', 'science', 'rainbow', 'water', 'pallindrome,''boat', 'programming', 'mathmatics', 'player',
             'condition']
    pick = random.choice(words)
    return pick


def jumbled(word):
    jumbled = "".join((random.sample(word, len(word))))
    return jumbled


def thank(p1, p2, ppn1, ppn2):
    print(p1, " your score is: ", ppn1)
    print(p2, " your score is: ", ppn2)
    if (ppn1 > ppn2):
        print(p1, " WON!!")
    elif(ppn1==ppn2):
        print("MATCH DRAW !!")
    else:
        print(p2, " WON!!")
    print("THANKS FOR PLAYING !!")


play()
