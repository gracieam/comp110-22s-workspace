"""A Night Sky with Stars."""

__author__ = "730402215"

from turtle import Turtle, colormode, done, circle, screensize

def main() -> None:
    from random import randint
    width: int = 300
    height: int = 300
    x: float = randint(-300, 300)
    y: float = randint(-300, 300)

def draw_sky(sky: Turtle, x: float, y: float) -> None:
    sky.goto(x, y)
    screensize(300, 300, "blue")


def draw_grass(landscape: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a green rectangle on a third of the dark blue background."""
    grass: Turtle = Turtle()
    grass.penup()
    grass.goto(x, y)
    grass.pendown()
    grass.fillcolor("green")
    grass.pencolor("green")

    grass.begin_fill()
    i: int = 0
    while i < 2:
        grass.forward(width)
        grass.right(90)
        grass.forward(height/2)
        grass.right(90)
        i += 1
    grass.end_fill()

def draw_stars(star: Turtle, x: float, y: float) -> None:
    """Draw yellow stars on dark blue background."""
    stars: Turtle = Turtle()
    stars.pencolor("yellow")
    stars.fillcolor("yellow")
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    
    stars.begin_fill()
    i: int = 0 
    while i < 5:
        stars.forward(15)
        stars.right(120)
        stars.forward(15)
        stars.right(72 - 120)
        i += 1
    stars.end_fill()

def draw_moon(the_moon: Turtle, x: float, y: float) -> None:
    """Draw a moon on dark blue background."""
    moon: Turtle = Turtle()
    moon.hideturtle()
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    colormode(255)
    moon.fillcolor(241, 246, 242)
    moon.pencolor(241, 246, 242)
    moon.begin_fill()
    moon.circle(75)
    moon.end_fill()


if __name__ == "__main__":
    main()

done()