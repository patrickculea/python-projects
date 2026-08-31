game = ["rock","paper","scissors"]
import random
comp = random.choice(game)
print("Lets play rock paper scissors")
user = input("Which do you choose? rock, paper or scissors?")
if user == comp:
    print(f"You tied with me. We both chose {user}.")
if user == "rock" and comp == "paper":
    print("You lose. I chose paper")
if user == "paper" and comp == "rock":
    print("You beat me. I chose rock")
if user == "paper" and comp == "scissors":
    print("You lost, I chose scissors.")
if user == "scissors" and comp == "paper":
    print("You beat me i chose paper.")
if user == "paper" and comp == "scissors":
    print("You lost, I chose scissors.")
if user == "rock" and comp == "scissors":
    print("You won, I chose scissors")
if user == "scissors" and comp == "paper":
    print("You won. I chose paper")
if user is not "scissors" and user is not "paper" and user is not "rock":
    print("Invalid input. You can only choose rock,paper or scissors.")


