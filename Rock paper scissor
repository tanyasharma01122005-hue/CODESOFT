# Firstly import random 
import random # it allows a computer to choose randomly 
# List of possible choices 
choices=["rock","paper","scissors"]
# Now it's time to take input from the user
user=input("Enter the choice from(rock/paper/scissor): ").lower()
computer_choice=random.choice(choices)
print(f"Computer's select:{computer_choice}")
if user==computer_choice:  
  print("match draw!")
elif user=="rock" and computer_choice=="scissors":
  print("You Win!")
elif user=="paper" and computer_choice=="rock":
  print("You Win!")
elif user=="scissor" and computer_choice=="paper":
  print("You Win!")
elif user in choices: # executes only if user entered a correct or valid choice but computer wins the match
  print("Computer wins the match!")
else:
  print("invalid ")
