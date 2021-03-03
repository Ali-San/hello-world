def remove_space(string):
    new_string = ""
    for char in string:
        if char == " ":
            continue
        else:
            new_string += char
    return new_string

string = "ab c  d e fgh i  j kl mn  opqr  stuvwxyz"

print(remove_space(string))