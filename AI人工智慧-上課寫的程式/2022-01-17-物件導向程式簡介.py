# from turtle import Screen, Turtle

from turtle import Screen , Turtle

scr1 = Screen()
t0 = Turtle()
t1 = Turtle()
t2 = Turtle()

scr1.colormode(255)
scr1.setup(1200,800)
scr1.bgcolor('Indigo')
# scr1.tracer(0)

#  畫出螢幕上的十字線
t0.speed(0)
t0.pencolor('black');t0.fillcolor('black')
t0.shape("turtle");t0.shapesize(1, 1, 1)
t0.forward(600)
t0.backward(1200)
t0.forward(600)
t0.left(90)
t0.forward(400)
t0.backward(800)
t0.forward(400)
t0.right(90)
t0.pencolor('white');t0.fillcolor('white')
t0.write('物件導向簡介', align='center', font=('Arial' , 50, 'normal' ) )
# turtle.write(arg, move=False, align='left', font=(r'C:\Windows\Fonts\msjhbd.ttc', 8, 'normal')) 無法更換成中文字體

angle1 = 0
t1.speed(0)
t1.pencolor('red');t1.fillcolor('red')
t1.shape("turtle");t1.shapesize(5, 5, 2)
t1.penup()
t1.goto( 200 ,200 )
t1.setheading(angle1)
t1.pendown()

angle2 = 0
t2.speed(0)
t2.pencolor('green');t2.fillcolor('green')
t2.shape("turtle");t2.shapesize(5, 5, 2)
t2.penup()
t2.goto( -200 ,-200 )
t2.setheading(angle2)
t2.pendown()

while True :
    angle1 += 10
    t1.setheading(angle1)
    angle2 -= 10
    t2.setheading(angle2)


scr1.mainloop()






















'''
screen = Screen()
t = Turtle('square')
t.speed(0)                          

def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight(x,y):
    t.clear()

def main():  # This will run the program

    #screen.listen()
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    screen.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()

'''



























'''


import random  #  讓程式知道我們將要使用random這個模組

# 自己喜歡的顏色名字  共 25 個
color_name = ['LightPink','Pink','Crimson','LavenderBlush','PaleVioletRed',
              'HotPink', 'DeepPink', 'MediumVioletRed', 'Orchid', 'Thistle',
              'Plum', 'Violet', 'Magenta', 'Fuchsia', 'DarkMagenta',
              'Purple', 'MediumOrchid', 'DarkViolet', 'DarkOrchid', 'Indigo',
              'BlueViolet', 'MediumPurple', 'MediumSlateBlue', 'SlateBlue', 'DarkSlateBlue']

import turtle  #  讓程式知道我們將要使用turtle這個模組

turtle.colormode(255)                   #  設定顏色的表示方法 (R,G,B)
turtle.setup(1200,800)                  #  設定螢幕的大小
turtle.speed(0)                         #  設定海龜移動的速度
turtle.pencolor('LightPink')            #  設定筆的顏色
turtle.fillcolor('LightPink')           #  設定填滿的顏色
turtle.shape("turtle")                  #  修改海龜的外型
turtle.shapesize(2, 2, 2)               #  改變海龜的大小及外框的粗細
turtle.bgcolor('DarkSlateBlue')         #  設定螢幕背景的顏色

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

turtle.listen()                         #  设置焦点到 TurtleScreen (以便接收按键事件)

turtle.onscreenclick(func0, btn=1)      #  滑鼠左鍵按下時，會呼叫 func0 這個函式

turtle.onkey(func1, "Up")               #  當往上的按鍵被按下，則會呼叫 func1 這個函式
turtle.onkey(func2, "Down")
turtle.onkey(func3, "Left")
turtle.onkey(func4, "Right")

turtle.mainloop()
'''