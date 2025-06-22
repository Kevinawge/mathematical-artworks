import math
import turtle
from PIL import Image

sunflower_bot = turtle.Turtle()
sunflower_bot.shape("turtle")
sunflower_bot.color("black")
sunflower_bot.speed(0)
sunflower_bot.screen.bgcolor("ivory")


def drawSunflower(t, numseeds, numpetals, angle, cspread):
    phi = angle * (math.pi / 180.0)
    for i in range(numseeds + numpetals):
        r = cspread * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        t.penup()
        t.goto(x, y)
        t.setheading(i * angle)
        t.pendown()

        if i < numseeds:
            t.dot(7, "saddlebrown")
        else:
            drawPetal(t, i)


def drawPetal(t, i):
    colors = ["gold", "orange"]
    t.fillcolor(colors[i % len(colors)])
    t.pencolor("darkorange")
    t.begin_fill()
    t.right(20)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.left(140)
    t.forward(70)
    t.left(40)
    t.forward(70)
    t.end_fill()
    t.setheading(0)


drawSunflower(sunflower_bot, 160, 60, 137.508, 4.5)
sunflower_bot.hideturtle()

canvas = turtle.getscreen().getcanvas()
canvas.postscript(file="sunflower.eps", colormode='color')

img = Image.open("sunflower.eps")
img.load(scale=2)
img.convert("RGB").save("sunflower.jpg", "JPEG")

turtle.done()
