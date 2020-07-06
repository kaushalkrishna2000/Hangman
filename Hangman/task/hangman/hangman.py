import random


def re(a, l, l1):
    l11 = list(l1)
    for i in range(len(l)):
        if (a == l[i]):
            l11[i] = a
    return "".join(l11)


def check(a):
    if (len(a) != 1):
        print("You should input a single letter")
        return 1
    elif not (a >= 'a' and a <= 'z'):
        print("It is not an ASCII lowercase letter")
        return 1
    else:
        return 0


print('''H A N G M A N\n''')
l = ['python', 'java', 'kotlin', 'javascript']
pr = '-'

word1 = l[random.randint(0, len(l) - 1)]
wor1 = pr * len(word1)
a = []
nog = 8

play=input("Type \"play\" to play the game, \"exit\" to quit:")

while(play=="play"):

    while (nog > 0):
        word = input("\n" + wor1 + "\nInput a letter:")

        flag = 0
        flag = check(word)

        temp = wor1
        wor1 = re(word, word1, wor1)

        if (temp == wor1 and flag == 0):
            if (word not in word1):
                if (word not in a):
                    print("No such letter in the word")
                    nog -= 1
                else:
                    print("You already typed this letter")
            elif (word in word1):
                print("You already typed this letter")

        a.append(word)

        if (word1 == wor1):
            break

    if (nog > 0):
        print("You guessed the word " + word1 + "! \nYou survived!")
    else:
        print("You are hanged!")

    play = input("Type \"play\" to play the game, \"exit\" to quit:")
