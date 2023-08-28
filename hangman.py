import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

print("Welcome to the game!\nGuess the word. HINT: It's name of a fruit.")

list = []
list2 = []

for i in word:
    print("_",end=' ')
    list2.append(i)
    if i not in list:
        list.append(i)

guesses = []

turns = int(len(list)) + 2
print(f"\nYou have only {turns} turns.")

correct = 0

while len(guesses) != len(list) and turns > 0:
    if turns == int(len(list)) + 2:
        g = input("Guess a character: ")
        while len(g) != 1:
            print("\nInvalid input!\nPlease enter a single alphabet.")
            g = input("\nGuess a character: ")
    else:
        g = input("\nGuess a character: ")
        while len(g) != 1:
            print("\nInvalid input!\nPlease enter a single alphabet.")
            g = input("\nGuess a character: ")
        
    if g in word:
        correct += 1
        turns -= 1
        print("Correct guess.")
        guesses.append(g)
        for j in list2:
            if j in guesses:
                print(j,end= ' ')
            else:
                print("_",end= ' ')
        pass
    else:
        turns -= 1
        print("Wrong guess.")

else:
    if len(list) == len(guesses):
        print(f"\nYou correctly guessed the word!\nThe word is {word}.")

    else:
        print(f"\nYou failed to guess the word in given number of tries.\nThe word was {word}.")