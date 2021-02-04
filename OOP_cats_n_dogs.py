'''
I wrote this program while learning OOP.
It's a silly thing that I came up with while trying to write a program
using classes and inheritance.
'''

import random
import time

class Pet():
    '''A parent class to describe pets.'''
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def walk(self):
        return "Cute {} {} was walking around the yard when".format(self.size, self.name)

    def eat(self):
        return "{} was eating when ".format(self.name)

    def sleep(self):
        return "{} was sound asleep when ".format(self.name)


class Dog(Pet):
    '''A child class to describe dogs.'''
    def __init__(self, name, size):
        super().__init__(name, size)

    def bark(self): #3
        return "{} began to bark loudly and".format(self.name)

    def chase(self, other): #3
        return "An angry {} chased an excited {} across the backyard,".format(self.name, other.name)
    
    def guard(self): #1
        return "{} was guarding the yard from the doorstep when ".format(self.name)


class Cat(Pet):
    '''A child class to describe cats.'''
    def __init__(self, name, size):
        super().__init__(name, size)
    
    def meow(self): #2
        return "The old {} {} meowed loudly.".format(self.size, self.name)
    def purr(self): #2
        return "Old {} {} began purring behind him.".format(self.size, self.name)
    
    def climb(self): #4
        return "{} climbed to the roof and run out of sight.".format(self.name)
    
    def tease(self, other): #2
        return "{} began teasing him from the window sill,\n\tdangling his tail just out of {}'s reach.".format(self.name, other.name)
    
    def walk(self): #2
        return "{} appeared slowly walking on the fence.".format(self.name)


tiny = Dog('Tiny', 'little')
kitty = Cat('Kitty', 'plump')

# I came up with 2 ways of organizing the data, and I chose to use both
# (I know it's not the most efficient thing to do, I could write a function and call it, but this works and I had already typed all of it, so...)

# first, dictionary of lists:
story = {'first line': [tiny.walk(),
                        tiny.guard(),
                        tiny.eat(),
                        tiny.sleep()],
        'second line': [kitty.walk(),
                        kitty.tease(tiny), kitty.purr()],
         'third line': [tiny.bark(),
                        tiny.chase(kitty)],
        'fourth line': [kitty.meow(),
                        kitty.climb()]}

# second, lists (clumsy and inefficient, I know, but for whatever reason I don't want to erase it)(list of lists would have been better):

fl_1 = tiny.walk()
fl_2 = tiny.guard()
fl_3 = tiny.eat()
fl_4 = tiny.sleep()

sl_1 = kitty.walk()
sl_2 = kitty.tease(tiny)
sl_3 = kitty.purr()
                 
tl_1 = tiny.bark()
tl_2 = tiny.chase(kitty)

fthl_1 = kitty.meow()
fthl_2 = kitty.climb()

first_line = [fl_1, fl_2, fl_3, fl_4]
second_line = [sl_1, sl_2, sl_3]
third_line = [tl_1, tl_2]
fourth_line = [fthl_1, fthl_2]

print("Hello, fellow netizen.\n")
time.sleep(1)
print("I tell short random stories about cats and dogs. Here's one:\n")
time.sleep(1)

print(first_line[random.randint(1, 4) - 1])
print(second_line[random.randint(1, 3) - 1])
print(third_line[random.randint(1, 2) - 1])
print(fourth_line[random.randint(1, 2) - 1])

time.sleep(3)
print("\nI hope you liked it.\nHere's another one:\n")
time.sleep(1)

print(story['first line'][random.randint(1, 4) - 1])
print(story['second line'][random.randint(1, 3) - 1])
print(story['third line'][random.randint(1, 2) - 1])
print(story['fourth line'][random.randint(1, 2) - 1])

print("\nFarewell my friend :)")