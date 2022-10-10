import turtle
import math

turtle.speed(0)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.turtlesize( 5 , 5 )
t1.hideturtle()

screen1 = turtle.Screen()

# screen1.setup(  width=1200, height=800, startx=100, starty=100   )
screen1.setup(  1200, 800, 100, 100   )

t1.color('blue')

t1.penup()
t1.goto(100,0)
t1.left(90)
t1.pendown()

t1.pensize(6)
t1.forward(130)
t1.circle(10,90)
t1.forward(180)
t1.circle(10,90)
t1.forward(260)
t1.circle(10,90)
t1.forward(180)
t1.circle(10,90)
t1.forward(130)

t1.color('red')

t1.penup()
t1.goto(0,-80)
t1.setheading(55)
t1.pendown()

d = 80 / math.cos(   math.radians(35) )
t1.begin_fill()
t1.forward( d )
t1.left(70)
t1.forward( d )
t1.left(110)
t1.forward( d )
t1.left(70)
t1.forward( d )
t1.left(110)
t1.end_fill()
t1.penup()

t1.goto(-50,70)
t1.write( "A ", True, align="center", font=('Arial', 40, 'normal') )

c = screen1.getcanvas()
item_id = c.create_text( 60, 100, text='A', fill='red',angle=180, font=("Arial", 40, "normal") )

screen1.mainloop()
