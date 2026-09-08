# This is my third project
# A game of Rock Paper and Scissor

# using random() function to get randomised answers
import random

# we want give user choices
options = ("rock", "paper", "scissor")

print("Welcome to game of Rock Paper and Scissor")

# for my code to run multile time i will use while loop
while True:
    Player_choice = input("Write your choice(or write quit): ").lower()

# user can select quit to quit the game else a invalid opertation
    if Player_choice == "quit":
        break

    if Player_choice not in options:
        print("invalid choice")
        continue

# we also want computer to pick a choice from options
    computer_choice = random.choice(options)
    print(computer_choice)

# segment of program where computer decides where it lost or won

# this one is when player wins
    if  Player_choice == "rock" and computer_choice == "scissor" or  Player_choice == "paper" and computer_choice == "rock" or Player_choice == "scissor" and computer_choice == "paper" :
        print("You win")

# this is when both pyer tie
    elif Player_choice == "rock" and computer_choice == "rock" or Player_choice == "paper" and computer_choice == "paper" or Player_choice == "scissor" and computer_choice == "scissor":
        print("Tie!!")

# the option left will let comptuer win
    else:
        print("Computer wins")
