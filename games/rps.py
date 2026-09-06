import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ").lower()

if user == computer:
    print(f"Tie! Both chose {computer}.")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print(f"You win! Computer chose {computer}.")
else:
    print(f"You lose! Computer chose {computer}.")
