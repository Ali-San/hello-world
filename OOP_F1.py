'''Idea from:

https://www.reddit.com/r/learnpython/comments/fetr93/struggling_to_implement_oop/?$deep_link=true&correlation_id=20e83bee-c99a-428e-a1de-9440056273a3&ref=email_digest&ref_campaign=email_digest&ref_source=email&utm_content=post_title&utm_medium=digest&utm_name=top_posts&utm_source=email&utm_term=day&$3p=e_as&$original_url=https%3A%2F%2Fwww.reddit.com%2Fr%2Flearnpython%2Fcomments%2Ffetr93%2Fstruggling_to_implement_oop%2F%3F%24deep_link%3Dtrue%26correlation_id%3D20e83bee-c99a-428e-a1de-9440056273a3%26ref%3Demail_digest%26ref_campaign%3Demail_digest%26ref_source%3Demail%26utm_content%3Dpost_title%26utm_medium%3Ddigest%26utm_name%3Dtop_posts%26utm_source%3Demail%26utm_term%3Dday&_branch_match_id=502151148411894068

Exercise description:
Simulate a race between a bunch of cars.
The cars travel at a random speed for every 1 minute long time step
across a track of given length and you need to list the order in which
the cars finish the race.
'''
import random
import time

drivers = ['Michael Schumacher',
           'Fernando Alonso',
           'Ayrton Senna',
           'Juan Manuel Fangio',
           'Niki Lauda',
           'Alain Prost',
           'Jacques Villeneuve',
           'Kimi Räikkönen',
           'Mika Hakkinen',
           'Rubens Barrichello'
           ]

constructors = ['Ferrari',
               'McLaren',
               'Mercedes',
               'Renault',
               'Alfa Romeo',
               'Williams Renault',
               'Honda',
               'Red Bull',
               'Benetton',
               'Haas'
               ]

car_top_speed = [random.randint(340, 375) for i in range(10)]

table = [drivers, constructors]

# race = 305km, 10 laps = 30.5 km
# speed: max = 375; min = 160

class Car():
    def __init__(self, driver, constructor, top_speed):
        self.constructor = constructor
        self.driver = driver
        self.top_speed = top_speed
        self.distance_traveled = 0
    
    def list_participants(self):
        print(self.driver, self.constructor, self.top_speed)
    
    def move(self, delta_time):
        self.distance_traveled += random.random() * self.top_speed * delta_time


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


random.shuffle(drivers)
random.shuffle(constructors)
    
participants = [Car(drivers[car], constructors[car], car_top_speed[car]) for car in range(10)]

print("The Racing Teams of Ali's Grand Prix are:")
print_table(table)

time.sleep(1)
print("\n🚥\tReady! Set! Go!")
time.sleep(1)
print("\nWhat an exciting race we are seeing today!\nEveryone's performance is at their very best!")
time.sleep(1)

print('\t\n🏁\n')

finish_line = []

for car in participants:
    position = []
    while car.distance_traveled < 305:
        car.move(0.1)
    position.append(round(car.distance_traveled, 2))
    position.append(car.driver)
    position.append(car.constructor)
    
    finish_line.append(position)

finish_line.sort(key=lambda x: x[0], reverse=True)

positions = enumerate(finish_line, start=1)

for n, position in positions:
    print(n, '\t', position[1].ljust(20), '  ', position[2].ljust(18))

time.sleep(1)
print()

for i in range(3):
    print(finish_line[i][1].ljust(20), '  🍾🏆')