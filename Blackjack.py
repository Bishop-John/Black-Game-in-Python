import random

playerScore1 = 0
playerScore2 = 0

name1 = input("Please enter your name: ")
name2 = input("Please enter your name: ")

for i in range(10):
    choice = input("Do you want to Hit or Stick? >")

    if choice == "h":
        newNumber = random.randint(1, 10)
        playerScore1 = playerScore1 + newNumber
        print(name1, "you were dealt a", newNumber)      
        print(name1,"your current total is:",playerScore1)
        
        if playerScore1 > 21:
            print("BUST!")
            exit()
           
    if choice == "s":
        print(name1, "has ", playerScore1)
        break

for i in range(10):
    choice = input("Do you want to Hit or Stick? >")

    if choice == "h":
        newNumber = random.randint(1, 10)
        playerScore2 = playerScore2 + newNumber
        print(name2, "you were dealt a", newNumber)      
        print(name2,"your current total is:",playerScore2)
        
        if playerScore2 > 21:
            print("BUST!")
            exit()
           
    if choice == "s":
        print(name2, "has ", playerScore2)
        break

if playerScore1 == playerScore2:
    print("It's a draw.")
elif playerScore1 > playerScore2:
    print(name1, "wins!")
else:
    print(name2, "wins!")





