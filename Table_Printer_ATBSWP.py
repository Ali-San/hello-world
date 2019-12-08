'''
Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
'''            
Your printTable() function would print the following:

# inner list are columns, i need to iterate :
					  nm
  apples Alice  dogs  00. 10. 20
 oranges   Bob  cats. 01. 11. 21
cherries Carol moose. 02. 12. 22
  banana David goose. 03. 13  23
  col_widths		   8.  5.  5
'''

def print_table(table):
	
	col_widths = []
	
	for column in table:
		max_word_len = 0
		for word in column:
			if len(word) > max_word_len:
				max_word_len = len(word)
		col_widths.append(max_word_len)

	n = 0
	m = 0
	while n < len(table[0]):
		for list in table:
			print(list[n].rjust(col_widths[m] + 2), end=' ')
			m += 1
		n += 1
		m = 0
		print('')

print_table(table_data)