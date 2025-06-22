import turtle
from PIL import Image

screen = turtle.Screen()
screen.setup(500, 800)
screen.tracer(0, 0)
screen.title('Hering Illusion - PythonTurtle.Academy')

turtle.hideturtle()
turtle.speed(0)


def hering():
    turtle.color('blue')
    for a in range(-85, 90, 5):
        turtle.up()
        turtle.goto(0, 0)
        turtle.setheading(a)
        turtle.down()
        turtle.forward(500)
        turtle.backward(1000)
        turtle.forward(500)

    turtle.color('red')
    turtle.pensize(5)
    for x in [-100, 100]:
        turtle.up()
        turtle.goto(x, -400)
        turtle.setheading(90)
        turtle.down()
        turtle.forward(800)


hering()
screen.update()

canvas = screen.getcanvas()
canvas.postscript(file="hering_turtle.eps")
img = Image.open("hering_turtle.eps")
img.convert("RGB").save("hering_turtle.jpg", "JPEG")

turtle.bye()
