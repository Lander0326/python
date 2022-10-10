import turtle
import math
turtle.speed(0)


t1 = turtle.Turtle()
t1.shape('turtle')
t1.turtlesize(3,3)
t1.hideturtle()

screen1 = turtle.Screen()

#screen1.setup(width=1200, height=800, startx=100, starty=100)
screen1.setup(1200,800,100,100)
t1.speed(0)

s = 0.2
d = 800 * s
r = d/math.tan(math.radians(67.5))

t1.color('red')

t1.penup()
t1.goto(0,-600*s)
t1.seth(45)
t1.pendown()

t1.begin_fill()
t1.forward(d)
t1.circle(r,225)
t1.left(180)
t1.circle(r,225)
t1.fd(d)
t1.end_fill()

# 寫A
t1.penup()
t1.goto(-150,180)
t1.color('black')
t1.write("A", True, align="center", font=('Arial', 70, 'normal') )

# 畫框
'''
t1.goto(0,0)
t1.color('red')
t1.setheading(0)
t1.forward(200)
t1.left(90)

t1.pensize(10)
t1.pendown()
t1.forward(300)
t1.circle(10,90)
t1.forward(390)
t1.circle(10,90)
t1.forward(580)
t1.circle(10,90)
t1.forward(390)
t1.circle(10,90)
t1.forward(300)
t1.penup()


screen1.mainloop()
'''

'''
數學模組中 必須會的基本函式
math.ceil()    最小 >= x (天花板)
math.floor()   最大 <= x (地板)
math.sqrt()    開庚號
math.degrees() 弧度轉角度
math.radians() 角度轉弧度
math.pi        呼叫常數 拍(3.14)
math.三角函數
'''