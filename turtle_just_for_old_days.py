'''This is just a silly code to play with the little turtle again. I used to use Logos in elementary school and now I found it on Python!'''

import turtle

turtle.shape('turtle')
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.color('blue')
turtle.backward(100)
turtle.right(120)
turtle.backward(100)
turtle.right(120)
turtle.backward(100)
turtle.right(120)

turtle.color('green')
turtle.right(60)
turtle.forward(200)
turtle.right(60)
turtle.backward(100)

turtle.color('red')

for i in range(24):
    turtle.forward(20)
    turtle.backward(20)
    turtle.left(15)

turtle.exitonclick()
