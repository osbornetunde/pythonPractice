# count = 0
# values = []
# for num in range(7):
# 	count += 1
# 	values.append('*' * count)
# 	print(''.join(values))
# for num in range(6):
# 	count -= 1
# 	print('*' * count)


def half_pyramid(rows):
	print('Half pyramid...\n')
	for i in range(rows):
		print('*' * (i+1))


half_pyramid(10)


def full_pyramid(rows):
	print('\nFull pyramid...\n')
	for i in range(rows):
		print(' '*(rows-i-1) + '*'*(2*i+1))

full_pyramid(6)


def inverted_pyramid(rows):
	print('\nInverted pyramid....\n')
	for i in reversed(range(rows)):
		print(' '*(rows-i-1) + '*' *(2*i+1))

inverted_pyramid(6)