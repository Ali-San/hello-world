'''
This program finds the alphabet position for each letter in a word (provided by the user),
and counts the number of vowels in it.
'''

def count_vowels(user_input):
    vowels = "aeiou"
    num = 0
    for char in user_input.lower():
        if char in vowels:
            num += 1
    print("Total number of vowels in '{}': {}.".format(user_input, num))

while True:
    user_input = input("Please enter a word: ")
    if user_input.isalpha():
        vowel_num = [str(ord(char) - 96) for char in user_input.lower()]
        print("Alphabet positions for '{}': ".format(user_input), end='')
        for num in vowel_num:
            print(num, end=' ')
        print(' ')
        count_vowels(user_input)
        break
    else:
        print("That's not a valid word.")