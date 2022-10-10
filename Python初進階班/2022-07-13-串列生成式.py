# squares = []
# for x in range(10):
#      squares.append(x**2)
#
# print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print([ (x,x**2) for x in range(10) ])


list1 = [ str(x) for x in range(2,11) ] + ['A','J','Q','K']
list2 = ['H','D','S','C']

print(   [  ( x , y )  for x in list2 for y in  list1 ]  )