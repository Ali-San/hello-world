'''
My answer to a challenge by John Wells from SoloLearn:

Easy Pattern

I figured I would make a pattern even beginners could handle. Trying to express in words may leave you confused so look at the examples for clarification.

Read a number 0 to 8. Make a pattern using the following open & close groupings: (), <>, [], and {}. You may pick your own order of the four groups, but that sequence must be maintained consistantly. The first line outputs as many of the groups as requested (repeating them for more than 4). The first column also lists the same sequence of groups for the requested lines. The rest of the field continues the pattern from the starting point of the first line and column. For example, zero might output (must output something):
   none

Four could get:
   ()<>[]{}
   <>[]{}()
   []{}()<>
   {}()<>[]

Eight could get:
   ()<>[]{}()<>[]{}
   <>[]{}()<>[]{}()
   []{}()<>[]{}()<>
   {}()<>[]{}()<>[]
   ()<>[]{}()<>[]{}
   <>[]{}()<>[]{}()
   []{}()<>[]{}()<>
   {}()<>[]{}()<>[]
'''

import random

size = random.randint(0, 8)

patterns = {1: ['[]', '[]', '[]', '<>'],
			2: ['A', 'A', 'V', 'A'],
			3: ['{}', '{}', '{}', '()'],
			4: ['@', '@', '#', '@']}

pat = patterns[random.randint(1, 4)]
pattern = ['()', '<>', '[]', '{}']

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