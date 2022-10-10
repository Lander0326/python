import turtle
import random
import 之寧模組
import time

#####################   主程式   ###########################

t1 = turtle.Turtle()  # 產生一個海龜物件
t1.hideturtle()

screen1 = turtle.Screen()
screen1.tracer(0) # 只看結果
screen1.setup( 1200, 800 )

list1 = [ str(x) for x in range(2,11) ] + ['J','Q','K','A'] # 索引編號排序
list2 = ['S','H','D','C']
list_d = [  (row,col)  for row in list1  for col in list2    ] # 交叉配對 Cross

list3 = []
n = 0
while len(list3) < 26 :         # 發牌
    item = random.choice(list_d)
    if item not in list3 :
        list3.append(item)
        n = n + 1

list_A = list3[::2]
list_B = list3[1::2]
#print(list3)
#print(list_A)
#print(list_B)
                                 # 排序
list_A.sort(   key = lambda x : (  list1.index(x[0]), list2.index(x[1])    )      )
list_B.sort(   key = lambda x : (  list1.index(x[0]), list2.index(x[1])    )      )
#print(list_A)
#print(list_B)

x0,y0=-550,200
for n in range(26) :    # 畫圖

        time.sleep(1)
        y0 = -y0
        i = n//2

        if n%2 == 0 :
            text = list_A[i][0]
            color = list_A[i][1]
        else :
            text = list_B[i][0]
            color = list_B[i][1]

        if color == 'H'  :
            之寧模組.畫紅心(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, text)
        elif color == 'D' :
            之寧模組.畫方塊(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, text)
        elif color == 'S' :
            之寧模組.畫黑桃(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, text)
        else :
            之寧模組.畫梅花(t1, screen1, x0 + 90 * int(n/2), y0, 0.4, text)



screen1.mainloop()


