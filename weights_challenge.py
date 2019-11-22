#I found this old Set of Weights. There are the following Weights in it:

#1x 10g
#2x 20g
#1x 50g
#2x 100g
#1x 200g

#Write a program that takes a Weight between 10g and 500g as Input and outputs the combination of Weights which fits best.

weights = [10, 20, 50, 100, 200]

combos = {10: weights[0],
		  20: weights[1],
		  30: [weights[0], weights[1]],
		  40: [weights[1], weights[1]],
		  50: weights[2],
		  60: [weights[0], weights[2]],
		  70: [weights[1], weights[2]],
		  80: [weights[0], weights[1], weights[2]],
		  90: [weights[1], weights[1], weights[2]],
		  100: weights[3],
		  200: weights[4],
		  300: [weights[3], weights[4]],
		  400: [weights[3], weights[3], weights[4]],
		  500: [weights[0], weights[1], weights[1], weights[2], weights[3], weights[3], weights[4]]
		}

input_weight = int(input("Enter the desired weight (min: 10g, max: 500g): "))

if input_weight % 10 != 0:
	print("This old set of weights cannot handle that, please give it a multiple of 10.")
	input_weight = int(input("Enter the desired weight (min: 10g, max: 500g): "))

def scale(input_weight):
	if input_weight in weights:
		print("You should just use the {}g one.".format(input_weight))
	else:
		if input_weight < 100:
			if input_weight == 30:
				print("You should use a {}g weight and a {}g weight.".format(weights[0], weights[1]))
			elif input_weight == 40:
				print("You should use 2 {}g weights.".format(weights[1]))
			elif input_weight == 60:
				print("You should use a {}g weight and a {}g weight.".format(weights[0], weights[2]))
			elif input_weight == 70:
				print("You should use a {}g weight and a {}g weight.".format(weights[1], weights[2]))
			elif input_weight == 80:
				print("You should use a {}g weight, a {}g weight and a {}g weight.".format(weights[0], weights[1], weights[2]))
			elif input_weight == 90:
				print("You should use 2 {}g weights and a {}g weight.".format(weights[1], weights[2]))
		elif 100 < input_weight < 200:
			print("You should use the following weights: {}, {}".format(combos[100], ''.join(str(combos[input_weight - 100]))))	
		elif 200 < input_weight < 300:
			print("You should use the following weights: {}, {}".format(combos[200], ''.join(str(combos[input_weight - 200]))))
		elif input_weight == 300:
			print("You should use the following weights: {}".format(combos[300]))
		elif 300 < input_weight < 400:
			print("You should use the following weights: {}, {}".format(combos[300], ''.join(str(combos[input_weight - 300]))))
		elif input_weight == 400:
			print("You should use the following weights: {}".format(combos[400]))
		elif 400 < input_weight < 500:
			print("You should use the following weights: {}, {}".format(combos[400], ''.join(str(combos[input_weight - 400]))))
		elif input_weight == 500:
			print("You should use the following weights: {}".format(combos[500]))

scale(input_weight)