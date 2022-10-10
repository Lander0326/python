# squares = []
# for x in range(10):
#      squares.append(x**2)
#
# print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print([ (x,x**2) for x in range(10) ])
#
#
# list1 = [ str(x) for x in range(2,11) ] + ['A','J','Q','K']
# list2 = ['H','D','S','C']
#
# print(   [  ( x , y )  for x in list2 for y in  list1 ]  )
#
# from math import *  # 學有關 math中所有函式
# 若 from math import ceil 只用math 中ceil 函式

# x = ceil(5.67)
# print(x)


# # from collections.abc import Iterable # for python >= 3.6
# import collections.abc
# num = [2, 4, 6]
#
# x = isinstance(num, list)
# print(num,'Instance of list?', x)
#
# x = isinstance(num, collections.abc.Iterable)
# print(num,'Instance of Iterable?', x)
#
# x = isinstance(num, (dict, list))
# print(num,'Instance of dict or list?', x)
#
# str1 = 'ABC'
#
# x = isinstance(str1, list)
# print(str1,'Instance of list?', x)
#
# x = isinstance(str1, collections.abc.Iterable)
# print(str1,'Instance of Iterable?', x)
#
# x = range(1,10)
# print(x)        # range(1, 10)
# print(list(x))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(type(x))
# a = isinstance(x, collections.abc.Iterable)
# print(x,'Instance of Iterable?', a)
#
# for i in range(1,10,2) :
#     print(i)

# 巢狀式迴圈
for row in range(5) :

    for col in range(10, 50, 10) :

        print(f'row={row}  col={col}')

list1 = [ str(x) for x in range(2,11) ] + ['A','J','Q','K']
list2 = ['H','D','S','C']

list_d = []
for row in list1 :
    for col in list2:
        list_d.append( (row,col) )

print(list_d)

list_dd = [ (row,col) for row in list1 for col in list2 ]
list_dd = [ (f'num{row},color-{col}') for row in list1 for col in list2 ] # 運算式使用F-string
list_dd = ['迴圈' for row in list1 for col in list2 ] # 運算式不用迴圈變數
print(list_dd)

list_d1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# 同下五行：
# list_d1 = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             list_d1.append([x,y])

vec = [-4, -2, 0, 2, 4]
print( [ x for x in range(-4,5,2) ] )

# 重要!! 2D_list 轉為 1D_list 的公式
vec = [[1,2,3], [4,5,6], [7,8,9]]
list_d2 = [num for elem in vec for num in elem]
print(list_d2)