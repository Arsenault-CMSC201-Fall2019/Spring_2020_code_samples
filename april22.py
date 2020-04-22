import turtle

bob = turtle.Turtle()
bob.fillcolor('blue')
bob.width(10)
bob.pencolor('green')
bob.begin_fill()
for i in range(5):
    bob.forward(200)
    bob.left(144)
bob.end_fill()

turtle.done()
