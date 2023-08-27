import random
l = int(input("Enter the lowest number of the range: "))
h = int(input("Enter the highest number of the range: "))

list = []
for i in range(l, h+1):
    list.append(i)

n = random.choice(list)
print(n)

t = 3
a = 1
print(f"You only have {t} tries.\nGood Luck!")
i = int(input("Guess the number: "))

if i == n:
    print("You guessed the correct number!\nIt took you only one try")

else:
    while i != n:
        if a == t:
            print("Your tries are exhausted.\nBetter luck next time!")
            exit()
        else:
            if i > n:
                print("Guess lower.")
                i = int(input("Guess the number: "))
                a = a+1
            else:
                print("Guess higher.")
                i = int(input("Guess the number: "))
                a = a+1
    print(f"You guessed the correct number!\nIt took you {a} tries.")