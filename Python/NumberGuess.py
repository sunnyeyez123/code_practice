'''This is a number guess game. If the user guesses higher than the sum of the dice rolled they win!'''

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print "The max value is " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "Try a smaller number!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "First rolled %d " % first_roll
    sleep(1)
    print "Second rolled %d " % second_roll
    sleep(1)
    total_roll = first_roll+ second_roll
    print "The total is %d" %total_roll
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "You Win!"
      return
    else:
      print "You lost..."
      return
    
roll_dice(6)  
    
    
  
  