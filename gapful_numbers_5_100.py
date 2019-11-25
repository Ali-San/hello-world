'''A gapful number is a number of at least 3 digits that is divisible by the number formed by the first and last digit of the original number.

For Example:
Input: 192
Output: true (192 is gapful because it is divisible 12)

Input: 583
Output: true (583 is gapful because it is divisible by 53)

Input: 210
Output: false (210 is not gapful because it is not divisible by 20)

Write a program to check if the user input is a gapful number or not.
'''

def is_gapful(number):
	str_num = str(number)
	first_last = str_num[0] + str_num[-1]
	if number % int(first_last) == 0:
		return True
	else:
		return False

print(is_gapful(192))
print(is_gapful(583))
print(is_gapful(210))
print(is_gapful(1980))
print(is_gapful(555))