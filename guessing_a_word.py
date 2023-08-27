import random

name = input("Enter your name: ")

print(f"Welcome to the game, {name}")

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

theWord = random.choice(words)
print(theWord)
turns1 = 12
turns2 = 12
length = int(len(theWord))

for i in range(0, length):
    print("_")

list = []
guesses = []

for i in theWord:
    list.append(i)

for i in range(0, length):
    g = input("Guess a character: ")
    while len(g) != 1:
        print("Invalid input!\nPlease enter a single alphabet.")
        g = input("Guess a character: ")
    if g == list[i]:
        guesses.append(g)
        print("Your guess is correct.")
        for k in guesses:
            print(k)
        for j in range(0, length - len(guesses)):
            print("_")
    else: 
        while g != list[i]:
            if turns2 == 1:
                break
            turns2 -= 1
            print(f"Wrong guess.\nYou are left with {turns2} turn(s).")
            for k in guesses:
                print(k)
            for j in range(0, length - len(guesses)):
                print("_")
            g = input("Guess a character: ")
            while len(g) != 1:
                print("Invalid input!\nPlease enter a single alphabet.")
                g = input("Guess a character: ")
        if turns2 == 1:
            break
        print("Your guess is correct.")
        guesses.append(g)
        for k in guesses:
            print(k)
        for j in range(0, length - len(guesses)):
            print("_")

if turns2 == 0:
    print(f"You failed.\nBetter luck next time.\nThe word was {theWord}.")
else:
    print(f"You guessed the word!\nThe word is {theWord}.")