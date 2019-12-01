'''
Inspired by a challenge from SoloLearn.
'''

import random

def random_pattern():
	
	patterns = {1: ['[]', '[]', '[]', '<>'],
				2: ['H', 'A', 'H', 'A'],
				3: ['{}', '()', '{}', '()'],
				4: ['@', '@', '#', '@'],
				5: ['()', '<>', '[]', '{}']}

	pat = patterns[random.randint(1, 4)]
	size = random.randint(0, 8)
	count = 0

	if size == 0:
		print('None')
	else:
		for i in range(size):
			count += 1
			for j in range(size):
				j += count
				print(pat[j%4], end='')
			print('')
	print('')


def choose_your_pattern(pat):
	
	size = random.randint(4, 8)
	count = 0
	print('')
	for i in range(size):
		count += 1
		for j in range(size):
			j += count
			print(pat[j%4], end='')
		print('')
	print('')
	print('Have a nice day!')


choice = int(input("Hello! Would you like to create a small pattern? (1)\nOr would you prefer me to do it for you? (2)\nEnter 1 or 2: "))

if choice == 1:
	user_pat = input("OK! Enter 4 characters to create your pattern.\nUse no spaces, please: ")
	if ' ' in user_pat:
		print("I told you no spaces. Good bye.")
	else:
		pat = []
		for char in user_pat:
			pat.append(char)
		choose_your_pattern(pat)

else:
	print("\nHere's what I created for you, hope you like it:\n")
	
	random_pattern()
	random_pattern()
	random_pattern()
	
	print("Have a nice day!")