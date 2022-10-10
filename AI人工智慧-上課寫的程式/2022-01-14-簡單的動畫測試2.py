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
turtle.hideturtle()             #  讓海龜隱形
turtle.bgcolor('Indigo')        #  設定螢幕背景的顏色
turtle.tracer(0)                #  海龜畫圖的過程不要看

'''
#  畫出螢幕上的十字線
turtle.forward(600)
turtle.backward(1200)
turtle.forward(600)
turtle.left(90)
turtle.forward(400)
turtle.backward(800)
turtle.forward(400)
turtle.right(90)
'''
x = 0 ; dx = 0.2
y = -50 ; dy = 0.2
while True :

    turtle.clear()            # 把指定的海龜其之前所畫的圖擦乾淨

    #  接下來是要畫一個方塊
    turtle.penup()                   #  筆抬起來
    turtle.goto( x ,y )              #  讓海龜走到指定的位置
    turtle.setheading(0)             #  讓海龜的頭朝向指定的方向
    turtle.pendown()                 #  筆放下去

    turtle.pencolor('Violet')    #  設定筆的顏色
    turtle.fillcolor('Violet')   #  設定填滿的顏色
    turtle.begin_fill()          #  設定開始填滿
    turtle.circle(50)
    turtle.end_fill()            #  結束填滿

    turtle.update()              #  把海龜畫好的圖，一次看清楚
    x = x + dx
    y = y + dy

    if x >= 550 or x <= -550 :
        dx = -dx
    if y >= 300 or y <= -400 :
        dy = -dy


turtle.mainloop()
