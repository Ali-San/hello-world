"""
I made this as a little "thank you" code,
you can try it on IDLE or https://skulpt.org/ if you want.
Thank you @Jay Matthews for the idea :)
"""


import turtle

turtle.shape('turtle')

n = 50
turtle.circle(n)

colors = ['blue', 'green', 'yellow', 'orange', 'red']

for j in range(5):
    turtle.color(colors[j])
    for i in range(1, 9):
        turtle.circle(3*i + n)
        turtle.left(72)

turtle.exitonclick()