# import the art from my file and random
from art import rock, paper, scissors
import random



# start the page with a user input - saved to variable - changed to int - set to next line
user_int = int(input("Want to play rock, paper, scissors? Type 0 for Rock, 1 for paper, or 2 for Scissors:\n"))

# set options to var in a list
options = ["rock", "paper", "scissors"]
art_options = [rock, paper, scissors]

# get computers random int 
computer_random_int = random.randint(0,2)

# if they match - tie game
if(user_int == computer_random_int):
  print(f"You chose:\n{art_options[user_int]}")
  print(f"The computer chose:\n{art_options[computer_random_int]}")
  print("It's a tie!")
# elif the user wins in these cases
elif (user_int == 0 and computer_random_int ==2) or (user_int == 1 and computer_random_int == 0) or (user_int == 2 and computer_random_int == 1):
  print(f"You chose:\n{art_options[user_int]}")
  print(f"The computer chose:\n{art_options[computer_random_int]}")
  print("You win!")
else:
  print(f"You chose:\n{art_options[user_int]}")
  print(f"The computer chose:\n{art_options[computer_random_int]}")
  print("You lose!")

