import turtle

turtle.colormode(255)  # 設定顏色的表示方法 (R,G,B)
turtle.setup(900, 900)
turtle.speed(9)
turtle.pencolor((160,185,51))  # 設定筆的顏色
turtle.fillcolor((160,185,51))  # 設定填滿的顏色
turtle.shape("turtle")  # 修改海龜的外型
turtle.shapesize(2, 2, 2)  # 改變海龜的大小及外框的粗細

#  畫中心十字線
turtle.forward(450)
turtle.backward(900)
turtle.forward(450)
turtle.left(90)
turtle.forward(450)
turtle.backward(900)
turtle.forward(450)
turtle.right(90)

#  先定位到起始的位置
turtle.penup()                    #  筆抬起來
turtle.goto(200,150)
turtle.setheading(90)
turtle.pendown()                  #  筆放下去

#  畫頭
turtle.begin_fill()
turtle.circle(200,180)
turtle.end_fill()

#  前進定位
turtle.penup()
turtle.forward(20)
turtle.pendown()

#  畫身體
turtle.begin_fill()
turtle.forward(300)
turtle.circle(50,90)
turtle.forward(300)
turtle.circle(50,90)
turtle.forward(300)
turtle.left(90)
turtle.forward(400)
turtle.end_fill()

#  前進定位畫左手
turtle.penup()
turtle.goto(-250,70)
turtle.setheading(250)
turtle.pendown()

turtle.pensize(75)
turtle.forward(190)

#  前進定位畫右手
turtle.penup()
turtle.goto(250,70)
turtle.setheading(70)
turtle.pendown()

turtle.pensize(75)
turtle.forward(190)

#  前進定位畫左腳
turtle.penup()
turtle.goto(-100,-200)
turtle.setheading(270)
turtle.pendown()

turtle.pensize(75)
turtle.forward(160)

#  前進定位畫右腳
turtle.penup()
turtle.goto(100,-200)
turtle.setheading(300)
turtle.pendown()

turtle.pensize(75)
turtle.forward(160)

#  前進定位畫左眼睛
turtle.penup()
turtle.goto(-80,240)
turtle.setheading(0)
turtle.pendown()

turtle.dot(45,"white")

#  前進定位畫右眼睛
turtle.penup()
turtle.goto(80,240)
turtle.setheading(0)
turtle.pendown()

turtle.dot(45,"white")

#  前進定位畫左天線
turtle.penup()
turtle.goto(-120,240)
turtle.setheading(120)
turtle.pendown()

turtle.pensize(15)

turtle.forward(150)

#  前進定位畫右天線
turtle.penup()
turtle.goto(120,240)
turtle.setheading(60)
turtle.pendown()

turtle.pensize(15)
turtle.forward(150)

#  小海龜回到原位，筆的大小調回0
turtle.penup()
turtle.goto(0,0)
turtle.setheading(0)
turtle.pensize(0)

turtle.mainloop()