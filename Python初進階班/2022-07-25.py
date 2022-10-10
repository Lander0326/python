import turtle
import random
import 之寧模組
import time

def aaa(x) :
    return (x[3],x[5])

表格 = 之寧模組.list_2D
欄位名稱 = 表格[0]
資料 = 表格[1:] # 切出第一排

#排序後的資料 = sorted(資料 ) # 按照地一個元素(姓名)排序
#排序後的資料 = sorted(資料,key = aaa)
排序後的資料 = sorted(資料, key = lambda x : (x[3],x[5])) # 按照地一個元素(姓名)排序

print(排序後的資料)

學生資料_T = list(zip(*排序後的資料))
for n in range(6):
    print(f'{欄位名稱[n]}:{學生資料_T[n]}')
# 所以排序完畢後,有需要轉置再轉置
#學生資料_T = list(zip(*學生資料))
#欄位名稱 = 學生資料_T[0][0]+學生資料_T[1][0]+學生資料_T[2][0]+學生資料_T[3][0]+學生資料_T[4][0]+學生資料_T[5][0]
#欄位名稱 = [ 學生資料_T[n][0] for n in range(len(學生資料_T))   ]





#list_1D = sorted(學生資料_T[0][1:])




'''
print(學生資料)
print(  list(zip(*學生資料))[0][1:]  )
學生資料_T = list(zip(*學生資料))
list(zip(*學生資料))[3][1:]
print(f'{學生資料_T[0][0]:10s}{學生資料_T[3][0]:10s}')
for n  in range(1,len(學生資料_T[0])) :
    print(f'{學生資料_T[0][n]:10s}{學生資料_T[3][n]:<10d}')  # F-string 參考 https://docs.python.org/3/library/string.html#formatspec
'''