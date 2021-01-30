'''
I wrote this program responding to a code challenge from SoloLearn.
This is my recursive approach to the Collatz conjucture.

https://en.wikipedia.org/wiki/Collatz_conjecture
'''


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

def collatz_seq(num):
    global counter
    counter += 1
    if num > 0 and type(num) == int:
        n = collatz(num)
        if n == 1:
            print("The End")
        else:
            collatz_seq(n)

counter = 0
try:
    user_num = int(input("Please enter a positive integer: "))
    if user_num <= 0:
        print("That's not a positive integer.\nTry again.")
        user_num = int(input("Please enter a positive integer: "))
    collatz_seq(user_num)
    print("\nNumber of times the function was called: {}".format(counter))
except ValueError:
    print("That's not a positive integer.\nI'll give you one more chance.")
    try:
        user_num = int(input("Please enter a positive integer: "))
        collatz_seq(user_num)
        print("\nNumber of times the function was called: {}".format(counter))
    except ValueError:
        print("That's not a positive integer.\nGood bye.")