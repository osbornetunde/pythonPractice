import random

input("Press any key to roll your dice:")
color=['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Black']
# op = random.randrange(1,7)
op1 = random.choice(color)
op = color.index(op1) + 1


print("Your Dice is", op1, "color with number", op)