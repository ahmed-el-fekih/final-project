import random
from datetime import datetime
class Calculator:
    def __init__(self):
        self.result = float(0)

    def add(self, x):
       self.result += float(x)

    def substract(self,x):
        self.result -= float(x)

    def get_result(self):
        return self.result

class BetterCalculator(Calculator):
    def multiply(self,x):
        self.result *= float(x)

    def divide(self,x):
        self.result /= float(x)

def question(a,b,c):
    print(a)
    b = random.randint(1,9)
    for guesses in range(3):
        answer = (input())
        if answer == str(c):
            print("\nThe number is " + str(b))
            break
        elif guesses < 2:
            print("\nTry again")
        else:
            print("\nYou're out of guesses")

name = input("What's your name?\n")

print("\n" + name + " ,you are one of a few that made it to the top of the mountain! Beyond this door, there are imaginable riches, but to get there, you have to solve the 'unbreakable puzzle' and crack its code!")
yes_or_no = input("Are you ready to solve the puzzle?\n")
if yes_or_no == "Yes":
    print("Great! I am going to start by explaining the puzzle to you.The puzzle consists of 3 questions, 2 riddles and 1 game, You have to answer or solve each one of them correctly to be able to decipher the code at the end. After each right answer, I'll give you a number, and you have to use all the numbers to decipher the code. P.S: You only have 3 chances per question!  ")

    question("\nQ1: Who's the best instructor in the edge program?" ,n1,"Meg" )
    question("\nQ2: How many continents are there?",n2, "7")
    question("\nQ3: Who was the mathematician that cracked the enigma code",n3,"Alan Turing")
    question("\nQ4: The monty hall problem. Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. Should you stick with the door you chose(door number 1), or switch doors(to door number 2). Type the number of the door you choose",n4,2)

    print("\nQ5: You have 10 tries to guess a random number between 1 and 1000")
    n5 = random.randint(1,1000)
    for guesses in range(10):
        guess = input()
        if int(guess) == n5:
            print("The number is " + str(n5))
        elif int(guess) > n5 and guesses < 9:
            print("That's too high, try again")
        elif int(guess) < n6 and guesses < 9:
            print("That's too low, try again")
        elif  int(guess) == 1001:
            while True:
                a = BetterCalculator()
                b = BetterCalculator()
                choice = input("Type the symbol of the operation that you want to do ")
                if choice == "+":
                    a.add(input("Choose a number "))
                    a.add(input("Choose another number "))
                    print("let's add these 2 numbers!")
                    answer1 = a.get_result()
                    print(answer1)
                elif choice == "-":
                    a.add(input("Choose a number "))
                    a.substract(input("Choose another number "))
                    print("let's substract the second number from the first!")
                    answer2 = a.get_result()
                    print(answer2)
                elif choice == "*":
                    b.add(input("Choose a number "))
                    b.multiply(input("Choose another number "))
                    print("let's multiply these 2 numbers!")
                    answer3 = b.get_result()
                    print(answer3)
                elif choice == "/":
                    b.add(input("Choose a number "))
                    b.divide(input("Choose another number "))
                    print("let's divide these 2 numbers!")
                    answer4 = b.get_result()
                    print(answer4)
                elif choice == "done":
                    break
                else:
                    print("This symbol is not supported by this calculator.")
        else:
            print("You're out of guesses")


else :
    print("These riches will be waiting for you to claim them another day!")












































































































































































































