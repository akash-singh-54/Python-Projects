import random

l = ["rock", "paper", "scissor"]
print("Choose one: ", l)
user= input("Enter your choice: ")
computer = random.choice(l)

if (user == "rock" and computer == "paper"):
    print("Computer choice is: ", computer)
    print("Computer won")

elif (user == "paper" and computer == "rock"):
    print("Computer choice is: ", computer)
    print("Usser won")

elif (user == "rock" and computer == "scissor"):
    print("Computer choice is: ", computer)
    print("Usser won")

elif (user == "scissor" and computer == "paper"):
    print("Computer choice is: ", computer)
    print("Usser won")

elif (user == "scissor" and computer == "rock"):
    print("Computer choice is: ", computer)
    print("Computer won")

elif (user == "paper" and computer == "scissor"):
    print("Computer choice is: ", computer)
    print("Computer won")

else:
    print("Computer choice is: ", computer)
    print("A Daraw")
    
