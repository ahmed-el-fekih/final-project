import random
from datetime import datetime

questions = ["\nQ1: Who's the best instructor in the edge program?\n","\nQ2: How many continents are there?\n","\nQ3: Who was the mathematician that cracked the enigma code\n","\nQ4: The monty hall problem. Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. Should you stick with the door you chose(door number 1), or switch doors(to door number 2). Type the number of the door you choose\n","\nQ5: You have 8 identical balls, but one of them is a bit heavier than the others. Using a scale, what is the minimum number of weighings you have to do in order to locate the heavier ball?\n",]

Answers = ["Meg",7,"Alan Turing",2,2]

n1 = random.randint(1,9)
n2 = random.randint(1,9)
n3 = random.randint(1,9)
n4 = random.randint(1,9)
n5 = random.randint(1,9)
n6 = random.randint(1,9)


def question(a,b):
    print(a)
    for guesses in range(3):
        answer = (input())
        if answer == str(b):
            print("\nThe number is ")
            if a == questions[0]:
                print(str(n1))
                break
            elif a == questions[1]:
                print(n2)
                break
            elif a == questions[2]:
                print(n3)
                break
            elif a == questions[3]:
                print(n4)
                break
            elif a == questions[4]:
                print(n5)
                break
        elif guesses < 2:
            print("\nTry again")
        else:
            print("\nYou're out of guesses")

name = input("\nWhat's your name?\n")

print("\n" + name + " ,you are one of a few that made it to the top of the mountain! Beyond this door, there are imaginable riches, but to get there, you have to solve the 'unbreakable puzzle' and crack its code!\n")
yes_or_no = input("Are you ready to solve the puzzle?\n")
if yes_or_no == "Yes":
    print("\nGreat! I am going to start by explaining the puzzle to you.The puzzle consists of 3 questions, 2 riddles and 1 game, You have to answer or solve each one of them correctly to be able to decipher the code at the end. After each right answer, I'll give you a number, and you have to use all the numbers to decipher the code. P.S: You only have 3 chances per question!\n  ")

    question(questions[0],Answers[0])
    question(questions[1],Answers[1])
    question(questions[2],Answers[2])
    question(questions[3],Answers[3])
    question(questions[4],Answers[4])

    print("\nQ5: You have 10 tries to guess a random number between 1 and 1000")
    game_answer = random.randint(1,1000)
    for guesses in range(10):
        guess = int(input())
        if guess == game_answer:
            print("The number is " + str(game_answer))
            break
        elif guess > game_answer and guesses < 9:
            print("That's too high, try again")
        elif guess < game_answer and guesses < 9:
            print("That's too low, try again")

        else:
            print("You're out of guesses")


else :
    print("These riches will be waiting for you to claim them another day!")
