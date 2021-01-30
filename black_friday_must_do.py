# Inspired by the book "Automate the boring stuff with Python"

def print_list(items_dict, left_width, right_width):
    print('SHOPPING LIST'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.title().ljust(left_width, '.') + str(v).rjust(right_width, ' '))

black_friday_wish_list = {'electronics': 2200, 'for the house': 250, 'toys': 320, 'clothes': 180, 'shoes': 130, 'hobbies': 190}

def how_much_is_it(items_dict, left_width, right_width):
    total = 0
    for v in items_dict.values():
        total += v
    print('\nTotal'.ljust(left_width, '.') + str(total).rjust(right_width, ' '))


print_list(black_friday_wish_list, 20, 5)
how_much_is_it(black_friday_wish_list, 21, 5)
print("\n\t...and that's when I decide not to buy anything!")