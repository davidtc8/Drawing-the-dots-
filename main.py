from turtle import Turtle, Screen
from color_list import color_list
import random

# this part of the project is where we recreate the painting
tim = Turtle()
screen = Screen()
iterations = 0
screen.bgcolor("#f7eeee")
tim.hideturtle()

def circles(color):
    tim.pendown()
    tim.color(color)
    tim.fillcolor((color))
    #tim.begin_fill()
    tim.dot(15, color)
    #tim.end_fill()
    tim.penup()
    tim.forward(35)

def movement():
    tim.penup()
    global iterations
    iterations += 25
    axisx = -700
    axisy = -350
    tim.goto(axisx, axisy + iterations)

def tim_movement():
    global tim
    global screen
    global color_list
    screen.colormode(255)
    tim.speed("fastest")
    tim.penup()
    tim.goto(-700, -350)
    tim.pendown()
    dividend = 0
    divisor = 10
    remainder = 10
    done = False
    while not done:
        random.shuffle(color_list)
        for color in color_list:
            dividend += .25
            divisor += .25
            if dividend == 300:
                done = True
                break
            elif dividend % divisor == remainder:
                remainder += 10
                movement()
            else:
                circles(color)

tim_movement()
screen.exitonclick()
