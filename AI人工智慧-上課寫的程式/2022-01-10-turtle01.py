import turtle 

turtle.setup(1200,800)
turtle.speed(2)
turtle.pencolor("red")          #  設定筆的顏色
turtle.fillcolor("green")        #  設定填滿的顏色
turtle.shape("turtle")            # 修改海龜的外型
turtle.shapesize(2, 2, 2)       #  改變海龜的大小及外框的粗細

turtle.forward(600)
turtle.backward(1200)
turtle.forward(600)
turtle.left(90)
turtle.forward(400)
turtle.backward(800)
turtle.forward(400)
turtle.right(90)

turtle.penup()                        #  筆抬起來
turtle.goto(-50,50)
turtle.pendown()                  #  筆放下去

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.pencolor("green")   
turtle.penup()                        #  筆抬起來
turtle.goto(-100,100)
turtle.pendown()                  #  筆放下去

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)

turtle.pencolor("blue")  
turtle.penup()                        #  筆抬起來
turtle.goto(-150,150)
turtle.pendown()                  #  筆放下去

turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)

turtle.mainloop()
