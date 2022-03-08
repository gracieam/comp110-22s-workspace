"""Turtle Tutorial"""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()
colormode(255)
leo.pencolor("blue")
leo.fillcolor(240, 153, 26)
leo.penup()
leo.goto(-150, -50)
leo.pendown()

leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()
colormode(255)
bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.speed(50)

side_length: float = 300.0

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i += 1

while (i < 10):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120)
    i +=1

done()
