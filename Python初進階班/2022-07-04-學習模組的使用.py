# 海龜模組的使用
import turtle
import turtle as tu
import math


t1 = tu.Turtle()
screen1 = tu.Screen()  # 類別產生物件
print(type(t1))
t1.speed(6)
screen1.colormode(255)
t1.fillcolor((255,0,0))

# 畫框
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

#中間
t1.goto(0,0)
t1.pendown()
t1.begin_fill()
t1.goto(50,0)
t1.goto(0,70)
t1.goto(-50,0)
t1.goto(0,-70)
t1.goto(50,0)
t1.end_fill()



#screen1 = turtle.Screen()  # 類別產生物件
screen1.mainloop()         # 物件產生方法
#tu.mainloop()    # 畫圖完畢後 不會立即關閉畫面
