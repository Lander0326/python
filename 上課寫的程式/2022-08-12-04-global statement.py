
'''
def sum_() :
    "當函式結束後，區域變數會自動回收"
    global  a,b,c
    a = a * 10
    b = b * 10
    c = c * 10
    t = a + b + c
    return t


a = 22
b = 11
c = 33

s = sum_()
print(a,b,c)
print(s)
'''

x = 0  # 全域變數

def outer():

    x = 1  # 區域變數

    def inner():
        nonlocal x
        # global x
        x = 2   # 區域變數
        print( "inner:", x )

    inner()
    print( "outer:", x )

outer()
print( "global:", x )

# inner: 2
# outer: 1
# global: 0