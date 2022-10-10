import random

# 自己喜歡的顏色名字  共 25 個
color_name = ['LightPink','Pink','Crimson','LavenderBlush','PaleVioletRed',
              'HotPink', 'DeepPink', 'MediumVioletRed', 'Orchid', 'Thistle',
              'Plum', 'Violet', 'Magenta', 'Fuchsia', 'DarkMagenta',
              'Purple', 'MediumOrchid', 'DarkViolet', 'DarkOrchid', 'Indigo',
              'BlueViolet', 'MediumPurple', 'MediumSlateBlue', 'SlateBlue', 'DarkSlateBlue']

import turtle

turtle.colormode(255)           #  設定顏色的表示方法 (R,G,B)
turtle.setup(1200,800)          #  設定螢幕的大小
turtle.speed(0)                 #  設定海龜移動的速度
turtle.pencolor('LightPink')    #  設定筆的顏色
turtle.fillcolor('LightPink')   #  設定填滿的顏色
turtle.shape("turtle")          #  修改海龜的外型
turtle.shapesize(2, 2, 2)       #  改變海龜的大小及外框的粗細
turtle.bgcolor('Indigo')        #  設定螢幕背景的顏色

def func1() :
    turtle.setheading(90)
    turtle.forward(100)
    return None

def func2():
    turtle.setheading(270)
    turtle.forward(100)
    return None

def func3():
    turtle.setheading(180)
    turtle.forward(100)
    return None

def func4():
    turtle.setheading(0)
    turtle.forward(100)
    return None

def func0(x,y):
    color = random.choice(color_name)
    turtle.pencolor(color)
    turtle.fillcolor(color)
    print("滑鼠左鍵")
    return None

turtle.listen()                #  设置焦点到 TurtleScreen (以便接收按键事件)

turtle.onscreenclick(func0, btn=1)

turtle.onkey(func1, "Up")      #  當往上的按鍵被按下，則會呼叫 func1 這個函式
turtle.onkey(func2, "Down")
turtle.onkey(func3, "Left")
turtle.onkey(func4, "Right")

turtle.mainloop()


