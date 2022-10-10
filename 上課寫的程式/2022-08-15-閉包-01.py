''' 一級物件舉例 '''

''' 函式為一級物件 2 '''

def func_out():

    def func_in():
        print('in')
        return None

    print('out')

    return func_in

ff = func_out() # 此時為 ff = func_in
ff()

''' 函式為一級物件 1，3，4 '''
# def func1():
#     print('func1')
#
# def func2():
#     print('func2')
#
# def func_m(f1,f2):
#     f1()
#     f2()
#     return None
#
# a = 100
#
# #list1 = [func1,func2] # 這兩個函式可以當結構中元素 函式可存在資料結構中
# ff1 = func1
# ff2 = func2
#
# # func_m(func1,func2)
# # func_m(list1[0],list1[1])
# func_m(ff1,ff2)


''' 串列為一級物件舉例 '''
# def func(list1):
#     list1.append([7,8,9])
#     return list1 # 2
#
# list1 = [1,2,3]
# list2 = [4,5,6]
# # 3
# list_m = [ list1,list2 ] # 4
# list_m = func(list_m) # 1
#
# print(list_m)