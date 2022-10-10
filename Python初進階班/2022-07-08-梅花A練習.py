import turtle
import math



t1 = turtle.Turtle()
t1.shape("turtle")
t1.turtlesize( 5 , 5 )
t1.hideturtle()

screen1 = turtle.Screen()
#screen1.tracer(0)
t1.speed(0)

# screen1.setup(  width=1200, height=800, startx=100, starty=100   )
screen1.setup(  1200, 800, 100, 100   )

# 畫框
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

# 畫梅花
t1.color('black')

d = 15 / math.sin(   math.radians(30) )

t1.penup()
t1.goto(0,-d/2)
t1.setheading(270)
t1.pendown()

t1.begin_fill()
t1.circle( d,300)
t1.left(180)
t1.circle( d,300)
t1.left(180)
t1.circle( d,300)
t1.left(180)
#梅花花體完畢，開始畫梗
t1.penup()
t1.goto(0,-d/2)
t1.setheading(260)
t1.pendown()

#t1.pencolor('red')

t1.forward(2*d)
t1.setheading(0)
t1.forward(d*math.sin(math.radians(10))*4)
t1.left(100)
t1.forward(2*d)


t1.end_fill()
t1.penup()

t1.goto(-50,70)
t1.write( "A ", False, align="center", font=('Arial', 40, 'normal') )

c = screen1.getcanvas()
item_id = c.create_text( 60, 100, text='A', fill='black',angle=180, font=("Arial", 40, "normal") )

screen1.mainloop()
