'''
import turtle as tu



t1 = tu.Turtle()
screen1 = tu.Screen()  # 類別產生物件
print(type(t1))
t1.speed(6)
screen1.colormode(255)
t1.fillcolor((255,0,0))

t1.penup()
t1.forward(100)
t1.left(90)
t1.pendown()
t1.forward(130)
t1.circle(10,90)
t1.forward(180)
t1.circle(10,90)
t1.forward(260)
t1.circle(10,90)
t1.forward(180)
t1.circle(10,90)
t1.forward(130)


t1.pencolor((255,0,0))

# 右下A
t1.penup()
t1.goto(80,-90)
t1.pendown()
t1.setheading(250)
t1.forward(25)
t1.setheading(110)
t1.forward(25)
t1.penup()
t1.goto(65,-100)
t1.pendown()
t1.setheading(0)
t1.forward(12)
t1.penup()


# 左上A
t1.goto(-80,90)
t1.pendown()
t1.setheading(70)
t1.forward(25)
t1.setheading(290)
t1.forward(25)
t1.penup()
t1.goto(-75,100)
t1.pendown()
t1.setheading(0)
t1.forward(13)
t1.penup()
#中間愛心







#screen1 = turtle.Screen()  # 類別產生物件
screen1.mainloop()         # 物件產生方法
#tu.mainloop()    # 畫圖完畢後 不會立即關閉畫面
'''

import turtle
import math

screen = turtle.Screen()
screen.title('Heart Animation - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

screen.tracer(0,0)
turtle.color('red')

def draw_heart(alpha,d):
  r = d/math.tan(math.radians(180-alpha/2))
  turtle.up()
  turtle.goto(0,-d*math.cos(math.radians(45)))
  turtle.seth(90-(alpha-180))
  turtle.down()
  turtle.begin_fill()
  turtle.fd(d)
  turtle.circle(r,alpha)
  turtle.left(180)
  turtle.circle(r,alpha)
  turtle.fd(d)
  turtle.end_fill()

a = 220
sign = -1
def animate():
  global a,sign
  turtle.clear()
  draw_heart(a,1000)
  screen.update()
  a += sign
  if a < 215:
    sign = -sign
  elif a > 220:
    sign = -sign
  screen.ontimer(animate,50)

animate()
turtle.mainloop()