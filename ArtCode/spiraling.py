import turtle
from PIL import Image, ImageOps

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("ivory")

turtle.speed(0)
turtle.hideturtle()
turtle.pensize(1)
turtle.pencolor("black")

step = 100
length = 100
angle = 120


def draw_pattern():
    for i in range(step):
        for b in range(2):
            turtle.forward(length + i * 2)
            turtle.right(angle + b)


draw_pattern()

canvas = turtle.getcanvas()
canvas.postscript(file="temp_output.eps", colormode='color')
turtle.bye()

img = Image.open("temp_output.eps")
img = img.convert("RGB")
img = ImageOps.expand(img, border=50, fill="ivory")  # ensures background fill
img = ImageOps.fit(img, (800, 800), centering=(0.5, 0.5))  # centered crop

img.save("spiral_pattern_fixed.jpg", "JPEG")
