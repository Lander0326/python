# from turtle import Screen, Turtle

from turtle import Screen , Turtle

scr1 = Screen()      # 產生螢幕物件
t1 = Turtle()        # 產生海龜一號
t2 = Turtle()        # 產生海龜二號

#  設定海龜一號的特性
angle1 = 225
t1.pencolor('red');t1.fillcolor('red')
t1.shape("turtle");t1.shapesize(5, 5, 2)
t1.penup()
t1.goto( 200 ,200 )
t1.setheading(angle1)
t1.pendown()
t1.pensize(20)

#  設定海龜二號的特性
angle2 = 45
t2.pencolor('green');t2.fillcolor('green')
t2.shape("turtle");t2.shapesize(5, 5, 2)
t2.penup()
t2.goto( -200 ,-200 )
t2.setheading(angle2)
t2.pendown()
t2.pensize(20)

# 設定海龜一號被拖曳時，要呼叫的函式
def drag_t1(x, y):
    t1.ondrag(None)      # t1 的 ondrag() 功能暫停
    t1.goto(x, y)
    t1.ondrag(drag_t1)   # t1 的 ondrag() 功能恢復
# 設定海龜一號被點擊時，要呼叫的函式
def click_t1(x, y):
    t1.clear()           # 清除海龜一號所畫的圖

t1.ondrag(drag_t1)     # 當海龜一號被拖曳時，呼叫 drag_t1 函式
t1.onclick(click_t1)   # 當海龜一號左鍵被點擊時，呼叫 click_t1 函式

# 設定海龜二號被拖曳時，要呼叫的函式
def drag_t2(x, y):
    t2.ondrag(None)
    t2.goto(x, y)
    t2.ondrag(drag_t2)
# 設定海龜二號被點擊時，要呼叫的函式
def click_t2(x, y):
    t2.clear()           # 清除海龜二號所畫的圖

t2.ondrag(drag_t2)     # 當海龜二號被拖曳時，呼叫 drag_t2 函式
t2.onclick(click_t2)   # 當海龜二號左鍵被點擊時，呼叫 click_t2 函式

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