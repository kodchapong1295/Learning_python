import colorgram

# # extract color from picture using colorgram
# rgb_colors = []
# colors = colorgram.extract('img1.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211), (243, 237, 241), (114, 83, 59), (201, 146, 177), (200, 77, 109), (145, 134, 72), (230, 90, 59), (141, 192, 140), (72, 103, 90), (68, 162, 92), (5, 165, 179), (227, 161, 183), (115, 126, 142), (163, 196, 221), (16, 66, 123), (187, 24, 34), (13, 56, 103), (235, 172, 160), (175, 201, 179), (163, 200, 215), (186, 27, 25), (80, 55, 37), (96, 61, 30)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()