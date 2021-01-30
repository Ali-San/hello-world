'''
I wrote this program responding to a code challenge from SoloLearn.
This is my iterative approach to the Collatz conjucture.

https://en.wikipedia.org/wiki/Collatz_conjecture
'''


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    iter_num = 0
    num = int(input("Enter a positive integer: "))
    initial_num = num
# to avoid 0 and negative integers:
    while num <= 0:
        print("That's not a positive integer, try again.")
        num = int(input("Enter a positive integer: "))
        initial_num = num
# begin Collatz sequence:
    if num == 1:
        num = collatz(num)
        iter_num += 1
    while num != 1:
        num = collatz(num)
        iter_num += 1
    if num == 1:
        print("\nNumber of iterations it took for {} to converge to 1: ".format(str(initial_num)) + str(iter_num)) # end of program
        
# to avoid floats
except ValueError:
    print("That's not an integer!")
    try:
        num = int(input("Enter a positive integer: "))
        initial_num = num
        while num <= 0:
            print("That's not a positive integer, try again.")
            num = int(input("Enter a positive integer: "))
            initial_num = num
# begin Collatz sequence:
        if num == 1:
            num = collatz(num)
            iter_num += 1
        while num != 1:
            num = collatz(num)
            iter_num += 1
        if num == 1:
            print("\nNumber of iterations it took for {} to converge to 1: ".format(str(initial_num)) + str(iter_num))
    except ValueError:
        print("That's not an integer.\nHave a nice day.")