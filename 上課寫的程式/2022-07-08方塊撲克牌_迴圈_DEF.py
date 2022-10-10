import turtle
import math

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


for n,item in enumerate('56289') :
    畫方塊(t1 ,screen1 , -450+225*n , 0 , 0.8 , item)


screen1.mainloop()