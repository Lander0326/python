import turtle
import math
import random

def 畫方塊(t1,screen1,x0,y0,scale1,text1):
    # 起始位置 X座標 y座標 , 大小比例, 點數

    # 畫邊框

    t1.color('blue')

    # step1. 起始位置方向設定好
    # 絕對位置設定為變數x0,y0後 再設定相對位置
    t1.color('blue')

    t1.penup()
    t1.goto(x0, y0)
    t1.setheading(0)  # 頭朝0向 (東)
    t1.forward(100 * scale1)
    t1.left(90)
    t1.pendown()

    # step2. 開始畫框
    t1.pensize(6 * scale1)
    t1.forward(130 * scale1)
    t1.circle(10 * scale1, 90)
    t1.forward(180 * scale1)
    t1.circle(10 * scale1, 90)
    t1.forward(260 * scale1)
    t1.circle(10 * scale1, 90)
    t1.forward(180 * scale1)
    t1.circle(10 * scale1, 90)
    t1.forward(130 * scale1)

    # 畫方塊

    # step1. 相對於原始位置的座標

    t1.color('red')

    t1.penup()
    t1.goto(x0, y0 - 80 * scale1)
    t1.setheading(55)
    t1.pendown()

    # step2. 算出方塊的邊長，開始畫方塊
    d = 80 * scale1 / math.cos(math.radians(35))
    t1.begin_fill()
    t1.forward(d)
    t1.left(70)
    t1.forward(d)
    t1.left(110)
    t1.forward(d)
    t1.left(70)
    t1.forward(d)
    t1.left(110)
    t1.end_fill()
    t1.penup()

    # 標左上A
    t1.goto(x0 - 50 * scale1, y0 + 70 * scale1)
    t1.write(text1, align="center", font=('Arial', math.floor(40 * scale1), 'normal'))

    # 標右下A 顛倒
    c = screen1.getcanvas()  # 叫出圖畫紙並翻轉
    item_id = c.create_text(x0 + 60 * scale1, -y0 + 100 * scale1, text=text1, fill='red', angle=180,
                            font=("Arial", math.ceil(40 * scale1), "normal"))

    return None


##############################    主程式    ###############################


t1 = turtle.Turtle()    #  產生一個海龜物件
t1.hideturtle()         #  隱藏海龜

screen1 = turtle.Screen()
screen1.tracer(0)
screen1.setup( 1200, 800 )

#list1 = [('A','H'),('2','H'),('3','H'),('4','H'),('5','H'),('6','H'),('7','H'),('8','H'),('9','H'),('10','H'),('J','H'),('Q','H'),('K','H'),
#         ('A','D'),('2','D'),('3','D'),('4','D'),('5','D'),('6','D'),('7','D'),('8','D'),('9','D'),('10','D'),('J','D'),('Q','D'),('K','D'),
#         ('A','S'),('2','S'),('3','S'),('4','S'),('5','S'),('6','S'),('7','S'),('8','S'),('9','S'),('10','S'),('J','S'),('Q','S'),('K','S'),
#         ('A','C'),('2','C'),('3','C'),('4','C'),('5','C'),('6','C'),('7','C'),('8','C'),('9','C'),('10','C'),('J','C'),('Q','C'),('K','C'),  ]

list1 = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']
random.choice(list1)
list2 = []
n = 0                            # 自行宣告n 變數去畫牌
while len(list2) < 5  :
    item = random.choice(list1)  # 隨機從list1 出牌存為item 串列
    if  item not in list2 :      # 如果list2串列中無出過的牌 則做以下
        list2.append(item)       # 把出的牌(item)存在list2中
        畫方塊(t1 ,screen1 , -450+225*n , 0 , 0.8 , item)
        n = n + 1                # 畫完一張在畫一張
screen1.mainloop()