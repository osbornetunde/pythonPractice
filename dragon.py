import random
import time

#we will create our own functions so we can simply call the code and not
#have to keep writing the same code over and over again.

def displayIntro():
	print('You are in a land full of dragons.')
	time.sleep(2)
	print('''In front of you see two caves. 
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is greedy and hungry, and will eat you on sight.''', '\n' )


def chooseCave():
	cave = " "
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave

def checkCave(chooseCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps in front of you: He opens his jaws and...')
	print()
	time.sleep(2)

	friendlycave = random.randint(1, 2)

	if chooseCave == str(friendlycave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	displayIntro() 

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print('Do you want to play again? (yes or no)')
	playAgain = input()



