"""A Night Sky with Stars."""

__author__ = "730402215"

from turtle import Turtle, colormode, done, screensize, tracer

tracer(0, 0)
drawing: Turtle = Turtle()


def main() -> None:
    """The act of drawing a starry night."""
    from random import randint
    draw_sky(drawing, 0, 0)
    draw_grass(drawing, -400, -100, 800, 750)
    draw_moon(drawing, 0, 100)
    number_of_stars(drawing)
    draw_stars(drawing, randint(100, 300), randint(100, 300))
    
    done()


def draw_sky(the_sky: Turtle, x: float, y: float) -> None:
    """Creates a solid blue background to be the night sky."""
    sky: Turtle = Turtle()
    sky.goto(x, y)
    screensize(0, 0, "blue")


def draw_grass(landscape: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a green rectangle on a third of the blue background to be the grass."""
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
        grass.forward(height / 3)
        grass.right(90)
        i += 1
    grass.end_fill()


def draw_stars(star: Turtle, x: float, y: float) -> None:
    """Draw yellow stars on a blue background."""
    stars: Turtle = Turtle()
    stars.pencolor("yellow")
    stars.fillcolor("yellow")
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    
    stars.begin_fill()
    i: int = 0 
    subtract_angle: int = 72
    while i < 5:
        stars.forward(15)
        stars.right(120)
        stars.forward(15)
        stars.right(subtract_angle - 120)
        i += 1
    stars.end_fill()


def number_of_stars(star: Turtle) -> None:
    """Creating a random number of stars."""
    from random import randint
    star_N: int = randint(10, 20)
    i: int = 0
    while i < star_N:
        draw_stars(drawing, randint(-350, 350), randint(100, 300))
        i += 1


def draw_moon(the_moon: Turtle, x: float, y: float) -> None:
    """Draw a moon on the blue background."""
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