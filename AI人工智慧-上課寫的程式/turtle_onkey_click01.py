import turtle
import random
from turtle import * 

tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

colors = ["red", "blue","green", "purple", "yellow", "orange", "black"]

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)


def clickLeft(x, y):  # Make sure to have parameters x, y
    tim.color(random.choice(colors))

def clickRight(x, y):
    tim.stamp()


turtle.listen()

turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3) # 3: Right Mouse Button

turtle.onkey(up, "Up")  
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # This will make sure the program continues to run 
