'''This is a program that allows a user to view their calendar, add events,update events and delete events'''

from time import sleep, strftime

NAME = "Jasmine"
calendar = {}

def welcome():
  print "Welcome, " + NAME
  print "THe calendar is opening..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Current time is: " + strftime("%H:%M: %S")
  sleep(1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    
    if user_choice == 'V':
      if len(calendar.keys()) <1:
        print "The calendar is empty."
      else:
        print calendar
        
    elif user_choice == 'U':
      date = raw_input("What date?")
      update = raw_input("Enter the udpate: ")
      calendar[date] = update
      print "Your calendar was updated!"
      print calendar
      
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) >10 or int(date[6:])< int(strftime("%Y")) :
        print "Invalid date entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again.upper()
        print try_again
        if try_again == "N":
          start = False
      else:
        calendar[date] = event
        print "Your calendar was updated!"
        print calendar  
        
    elif user_choice == 'D':
      if len(calendar.keys()) <1:
        print "The calendar is empty."
      else:
        event = raw_input("Enter event: ")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "The event was deleted."
            print calendar
          else:
            print "The event specified was incorrect"
        
    elif user_choice == 'X':
      start = False
    else:
      print "That command was not valid."
      start = False
      
start_calendar()
      
        
    
    
    
  
  
  