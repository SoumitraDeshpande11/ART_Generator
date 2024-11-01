import turtle
import random
import math

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Perfect Diya Art Generator")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

colors = ["#FF6F61", "#F7CAC9", "#92A8D1", "#034F84", "#F7786B", "#DE3163", "#6495ED", "#FFE4B5", "#8B0000", "#FFF"]

def draw_diya(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(size, steps=3)
    pen.end_fill()
    pen.penup()
    pen.goto(x, y + size * 1.5)
    pen.pendown()
    pen.color("#FFD700")
    pen.begin_fill()
    pen.circle(size / 2, steps=3)
    pen.end_fill()
    pen.penup()
    pen.goto(x - size * 0.6, y - size * 0.4)
    pen.pendown()
    pen.color("white")
    pen.circle(size, steps=5)

def draw_concentric_circles(radius, layers, colors):
    for i in range(layers):
        pen.penup()
        pen.goto(0, -radius + i * 15)
        pen.pendown()
        pen.color(random.choice(colors))
        pen.circle(radius - i * 15)

def draw_mandala_petals(radius, colors):
    for j in range(36):
        pen.penup()
        angle = j * 10
        x = (radius - 50) * math.cos(math.radians(angle))
        y = (radius - 50) * math.sin(math.radians(angle))
        pen.goto(x, y)
        pen.setheading(angle)
        pen.pendown()
        pen.color(random.choice(colors))
        pen.begin_fill()
        pen.circle(10, steps=3)
        pen.end_fill()

def arrange_diyas_in_circle(center_x, center_y, radius, num_diyas):
    angle = 360 / num_diyas
    for i in range(num_diyas):
        x = center_x + radius * math.cos(math.radians(i * angle))
        y = center_y + radius * math.sin(math.radians(i * angle))
        draw_diya(x, y, 20, random.choice(colors))

draw_concentric_circles(200, 12, colors)
draw_mandala_petals(200, colors)
arrange_diyas_in_circle(0, 0, 250, 14)

ts = turtle.getcanvas()
ts.postscript(file="perfect_diya_art.eps")

turtle.done()

