'''
Goldbach's conjecture is a rule in math that states the following: every even number greater than 2 can be expressed as the sum of two prime numbers. 

Write a program that finds every possible pair of prime numbers, whose sum equals the given number or a set of numbers within a range.

For example:
Input: 16
Output:
3 + 13
5 + 11

Input: 32
Output: 
3 + 29
13 + 19

Input: 4, 8
Output: 
4: 2 + 2  
6: 3 + 3  
8: 3 + 5
'''

def check_if_prime(num):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return False
		else:
			return True
	else:
		return False

def goldbach(input_num):
	
	lesser_nums = [x for x in range(1, input_num)]
	lesser_nums_inv = [x for x in range(input_num - 1, 0, -1)]

	all_output = []

	for i in lesser_nums:
		for j in lesser_nums_inv:
			if (i + j) == input_num:
				if check_if_prime(i) and check_if_prime(j):
					
					output = []
					a, b, c = input_num, i, j
					output.append(a)
					output.append(b)
					output.append(c)
					all_output.append(output)

	final_output = []

	for i in range(len(all_output)):
		all_output[i].sort()
	for item in all_output:
		final_output.append(tuple(item))

	final_output = list(set(final_output))

	print("Input: {}".format(final_output[0][2]))
	print("Output:")
	for item in final_output:
		print("{} + {}".format(item[0], item[1]))
	return None


choice = int(input("Would you like to enter a number (1) or a range of numbers (2)?"))

if choice == 1:
	input_num = int(input("Enter an even number greater than 2: "))
	goldbach(input_num)
elif choice == 2:
	input_nums = input("Enter 2 even numbers, both greater than 2, separated by a space, like this: '6 10':")
	working_range = input_nums.split()
	a, b = int(working_range[0]), int(working_range[1])
	for num in range(a, b+2):
		if num % 2 == 0:
			goldbach(num)