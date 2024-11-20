print("Welcome to the Rock, Paper, Scissors Jam")
print("On your mark, get set, go!")


#1
user_choice = input("It is a game of chance. Will you choose rock, paper, or scissors?")
import random


choices = ["rock", "paper", "scissors"]


computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")


if user_choice == "rock" and computer_choice == "paper":
   print("You Win!")
   if user_choice == "paper" and computer_choice == "rock":
       print("You Win!")
   elif user_choice == "scissors" and computer_choice == "paper":
       print("You Win!")
   elif user_choice == computer_choice:
       print("It's a Tie!")
else:
   print("You Lose!")
