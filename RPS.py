'''This is a simple game of rock, paper, scissors!'''

from random import randint
from time import sleep

OPTIONS = ["R", "P", "S"]
LOSER = "You lost."
WINNER = "You won!"

def decide_winner(user_choice, computer_choice):
  print "User chose: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer chose: %s" %computer_choice
  user_choice_index = OPTIONS.index(user_choice) if user_choice in OPTIONS else -1
  computer_choice_index = OPTIONS.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WINNER
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WINNER
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WINNER
  elif user_choice_index < 0:
    print "That not a valid option."
    return
  else:
    print LOSER

def play_RPS():
  print "Rock, Paper, Scissors!"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice =OPTIONS[randint(0,len(OPTIONS)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()
  
  
  
