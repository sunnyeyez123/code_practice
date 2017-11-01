'''Character Input Create a program that asks the user to enter their name and
their age. Print out a message addressed to them that tells them the year that
they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing 
out that many copies of the previous message. '''

name, age, count = raw_input("Please enter your 'name, age, number'. ex: Jaz, 26, 2: ").split(',')

one_hundred = 100 -int(age)

for n in range(int(count)):
	print "Hello %s! You will be 100 years old in %d years" % (name, one_hundred)