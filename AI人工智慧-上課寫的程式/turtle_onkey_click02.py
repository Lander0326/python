import turtle

screen = turtle.Screen()
screen.setup (500,500)
screen.colormode(255)

t1 = turtle.Turtle()
t1.speed(0)
t1.width(1)
t1.hideturtle()
t1.penup()

r = g = b = 255
screen.bgcolor(r,g,b)

def clickLeft( x, y ):  # Make sure to have parameters x, y
    global r,g,b
    t1.clear()

    if x > 0 :
        r += 10
    else :
        r -= 10

    if r > 255 :
        r = 255
    elif r < 0 :
        r = 0

    t1.goto(0,50)
    str1 = "background color of the Screen"
    t1.write(str1, True, align="center", font=("Arial", 20, "normal"))

    t1.goto(0,0)
    str2 = str(r)+" , "+str(g)+" , "+str(b)
    t1.write(str2, True, align="center", font=("Arial", 30, "normal"))

    screen.bgcolor(r,g,b)
    
def clickMiddle(x, y):
    global r,g,b
    t1.clear()

    if x > 0 :
        g += 10
    else :
        g -= 10

    if g > 255 :
        g = 255
    elif g < 0 :
        g = 0

    t1.goto(0,50)
    str1 = "background color of the Screen"
    t1.write(str1, True, align="center", font=("Arial", 20, "normal"))

    t1.goto(0,0)
    str2 = str(r)+" , "+str(g)+" , "+str(b)
    t1.write(str2, True, align="center", font=("Arial", 30, "normal"))

    screen.bgcolor(r,g,b)
    
def clickRight(x, y):
    global r,g,b
    t1.clear()

    if x > 0 :
        b += 10
    else :
        b -= 10

    if b > 255 :
        b = 255
    elif b < 0 :
        b = 0

    t1.goto(0,50)
    str1 = "background color of the Screen"
    t1.write(str1, True, align="center", font=("Arial", 20, "normal"))

    t1.goto(0,0)
    str2 = str(r)+" , "+str(g)+" , "+str(b)
    t1.write(str2, True, align="center", font=("Arial", 30, "normal"))

    screen.bgcolor(r,g,b)

screen.onscreenclick(clickLeft,1)
screen.onscreenclick(clickMiddle,2)
screen.onscreenclick(clickRight,3)

turtle.mainloop()