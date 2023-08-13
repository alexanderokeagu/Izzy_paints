# import colorgram
#
# colors = colorgram.extract('image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

paint = t.Turtle()
paint.speed("fastest")
paint.penup()
paint.hideturtle()
t.colormode(255)
color_list = [(201, 157, 157), (63, 104, 104), (128, 160, 160), (153, 86, 86), (124, 82, 82), (132, 173, 173),
              (223, 198, 198), (188, 141, 141), (189, 134, 134), (47, 31, 31), (182, 93, 93), (64, 124, 124),
              (19, 46, 46), (62, 158, 158), (204, 95, 95), (147, 25, 25), (11, 24, 24), (232, 173, 173), (44, 28, 28),
              (87, 143, 143), (139, 33, 33), (170, 206, 206), (106, 126, 126), (221, 175, 175), (26, 80, 80),
              (53, 63, 63)]

paint.setheading(225)
paint.fd(300)
paint.setheading(0)
num_of_dots = 100

for _ in range(1, num_of_dots + 1):
    paint.dot(20, random.choice(color_list))
    paint.fd(50)

    if _ % 10 == 0:
        paint.setheading(90)
        paint.fd(50)
        paint.setheading(180)
        paint.fd(500)
        paint.setheading(0)

screen = t.Screen()
screen.exitonclick()
