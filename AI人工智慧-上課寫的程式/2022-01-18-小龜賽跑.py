#  小龜賽跑
#  https://trinket.io/docs/colors  選顏色的網站
import turtle
import random

turtle.colormode(255)           #  設定顏色的表示方法 (R,G,B)
turtle.setup(1200,800)          #  設定螢幕的大小
turtle.speed(0)                 #  設定海龜移動的速度
turtle.bgcolor('Indigo')        #  設定螢幕背景的顏色
turtle.pencolor('white')        #  設定筆的顏色
turtle.fillcolor('white')       #  設定填滿的顏色
turtle.tracer(0)                #  海龜畫圖的過程不要看

for step in range(15):
    turtle.write(step, align="center", font=("Arial", 12, "normal"))
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    trigger = -1
    for step2 in range(20):
        trigger = trigger * -1
        if trigger == 1:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(20)
    turtle.penup()
    turtle.backward(420)
    turtle.left(90)
    turtle.forward(40)

turtle.mainloop()

