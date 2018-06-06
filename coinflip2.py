import random
print('''I will flip a coin 1000 times...Guess how many times it will come
	up heads.(press Enter to begin)''')
n = int(input("Enter your guess: "))
flips = 0
heads = 0
while flips < 1000:
	if random.randint(0,1)==1:
		heads += 1
	flips += 1
	if flips == 900:
		print("900 flips and there have been "+ str(heads)+" heads.")
	if flips == 100:
		print("At 100 tosses, heads has come up " + str(heads) + ' times so far.')
	if flips == 500:
		print("Half-way done, and heads has come up " + str(heads)+ ' times.')
if flips == 1000:
	if n == int(heads):
		print("You guessed right!")
	elif n in range((int(heads)-10), (int(heads) + 10)):
		print("You were very close!")
	else:
		print("You guessed wrong")

print()
print("out of 1000 coin tosses: ")
print('\t',"Heads came up: ", heads)
tails = (1000-int(heads))
print('\t','Tails came up: ',tails, '\n')
