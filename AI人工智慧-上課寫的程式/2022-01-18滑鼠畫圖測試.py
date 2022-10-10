from turtle import Screen, Turtle

colors = ["red", "green", "blue"]
n = 0
scr1 = Screen()
t1 = Turtle(shape = 'circle')
t1.speed(0)
t1.pencolor(colors[n]);t1.fillcolor(colors[n])
t1.shapesize(1, 1, 1);t1.pensize(16)

def dragging(x, y):  # These parameters will be the mouse position
    t1.ondrag(None)
    t1.setheading(t1.towards(x, y))
    t1.goto(x, y)
    t1.ondrag(dragging)

def t1ClickMid(x,y):
    global n
    if n == 0 :
        n = 1
    elif n == 1 :
        n = 2
    else :
        n = 0

    t1.pencolor(colors[n]);t1.fillcolor(colors[n])

def screenClickLeft(x,y):
    t1.ondrag(None)
    t1.setheading(t1.towards(x, y))
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.ondrag(dragging)

def screenClickRight(x,y):
    t1.clear()

def main():  # This will run the program

    #screen.listen()
    t1.ondrag(dragging)  # When we drag the turtle object call dragging
    t1.onclick(t1ClickMid, 2)
    scr1.onscreenclick(screenClickLeft, 1)
    scr1.onscreenclick(screenClickRight, 3)

    scr1.mainloop()  # This will continue running main()

main()

'''

from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def main():
    global colors
    shape("circle")
    resizemode("user")
    shapesize(.5)
    width(3)
    colors=["red", "green", "blue", "yellow"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

'''