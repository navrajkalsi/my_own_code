import random

num = str(random.randrange(1000, 10000))
numList = []

for k in num:
    numList.append(k)

# print(num)
list = []
correct = []
tries = 1

n = input("Guess the 4 digit number: ")

if len(n) != 4:
    n = input("Invalid input.\nPlease enter a valid 4 digit number: ")
else:
    pass

if n == num:
    print("Great! You guessed the number in just 1 try! You are a mastermind!")

else:
    while n != num:
        tries += 1
        for i in n:
            list.append(i)

        for j in range(0,4):
            j = int(j)
            if numList[j] == list[j]:
                correct.append(numList[j])
        
        print(f"Not quite the number. But you did get {len(correct)} digits correct!\nAlso these number in your input were correct:")

        for j in range(0,4):
            j = int(j)
            if numList[j] == list[j]:
                print(numList[j], end=" ")
            else:
                print("X", end=" ")
        list.clear()
        correct.clear()
        
        n = input("\nEnter the next choice of numbers: ")
        if len(n) != 4:
            n = input("Invalid input.\nPlease enter a valid 4 digit number: ")
        else:
            pass

    if tries <= 5:
        print(f"You have become a Mastermind.\nIt took you only {tries} tries.")
    else:
        print(f"You have become a Mastermind.\nIt took you {tries} tries.")