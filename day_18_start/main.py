import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

# #Draw dash-line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# #Draw a shape from 3 to 10 side with random color
# colors = ["coral", "wheat", "SeaGreen", "red", "DarkOrchid"]
# for i in range(3,10):
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)

# # Draw a random line with random set of colors
# colors = ["coral", "wheat", "SeaGreen", "red", "DarkOrchid", "IndianRed", "DeepSkyBlue","SlateGray", "CornflowerBlue"]
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random.choice(colors))

# #draw randon line with random rgb color
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
#
#
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)











screen = Screen()
screen.exitonclick()