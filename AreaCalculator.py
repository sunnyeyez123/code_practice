'''This is a program that calculates the area of triangles and circles'''

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "The calculator is starting"
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()
print option

if option == 'C':
  radius = float(raw_input("What is the radius: "))
  area = pi * (radius**2)
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area,hint))
elif option == 'T':
  base = float(raw_input("What is the base: "))
  height = float(raw_input("What is the height: "))
  area = .5 * base * height
  print "Uni Bi Tri..."
  sleep(1)
  print("Area: %.2f \n%s"  % (area, hint))
else:
  print "You entered garbage! Goodbye."
  
  
    


  
