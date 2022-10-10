import turtle
import math

def 畫黑桃(t1, screen1, x0, y0, scale, text1):

    # 畫邊框

    # step1. 起始位置與方向設定好

    t1.color('blue')
    t1.penup()
    t1.goto(x0, y0)
    t1.setheading(0)
    t1.forward(100 * scale)
    t1.left(90)
    t1.pendown()

    # step2. 開始畫框

    t1.pensize(6 * scale)
    t1.forward(130 * scale)
    t1.circle(10 * scale, 90)
    t1.forward(180 * scale)
    t1.circle(10 * scale, 90)
    t1.forward(260 * scale)
    t1.circle(10 * scale, 90)
    t1.forward(180 * scale)
    t1.circle(10 * scale, 90)
    t1.forward(130 * scale)

    # 畫黑桃

    # step1. 相對於原始位置的座標與方向設好

    t1.color('black')

    t1.penup()
    t1.goto(x0 + 0, y0 + 80 * scale)
    t1.setheading(225)
    t1.pendown()

    # step2. 算出黑桃弧線的半徑，開始畫黑桃

    d = 80 * scale  # 注意，在這裡 d 值已經縮放
    r = d / math.tan(math.radians(67.5))  # 因 d 值已經縮放，r 值也就縮放了

    t1.begin_fill()
    t1.forward(d)
    t1.circle(r, 225)
    t1.left(180)
    t1.circle(r, 225)
    t1.forward(d)
    t1.end_fill()
    t1.penup()

    # step3. 開始畫黑桃的底座

    t1.penup()
    t1.goto(x0, y0)
    t1.setheading(260)
    t1.pendown()

    t1.begin_fill()
    t1.forward(d)
    t1.setheading(0)
    t1.forward(d * math.sin(math.radians(10)) * 2)
    t1.left(100)
    t1.forward(d)
    t1.end_fill()
    t1.penup()

    # 寫文字，順便測試一下 math.floor  math.ceil

    t1.goto(x0 - 60 * scale, y0 + 70 * scale)
    t1.write(text1, align="center", font=('Arial', math.floor(40 * scale), 'normal'))

    c = screen1.getcanvas()
    item_id = c.create_text(x0 + 60 * scale, -y0 + 100 * scale, text=text1, fill='black', angle=180,
                            font=("Arial", math.ceil(40 * scale), "normal"))

    return None


#####################   主程式   ###########################

t1 = turtle.Turtle()  # 產生一個海龜物件

t1.hideturtle()

screen1 = turtle.Screen()
screen1.tracer(0)  # 只看結果
screen1.setup(1200, 800)
#畫黑桃(t1, screen1, 0, 0, 2, 'A')  # 測試畫大張的看看

for n, item in enumerate('56789'):
    畫黑桃(t1, screen1, -450 + 225 * n, 0, 1, item)

screen1.mainloop()
