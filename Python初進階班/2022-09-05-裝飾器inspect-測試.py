def foobar(a: int, b: "it's b", c: str = 5) -> tuple:
    return a, b, c


import inspect
sig = inspect.signature(foobar)
# 获取函数参数
print(sig.parameters)
# OrderedDict([('a', <Parameter "a:int">), ('b', <Parameter "b:"it's b"">), ('c', <Parameter "c:str=5">)]))
# 获取函数参数注解


for k, v in sig.parameters.items():
    print('{k}: {a}'.format(k=k, a=v.annotation))
    # a: <class 'int'>
    # b: "it's b"
    # c: <class 'str'>
print(sig.return_annotation)# 返回值注解
# <class 'tuple'>
'''
###########
inspect模組
###########
import turtle
import inspect
a = inspect.ismodule(inspect)     # 檢查inspect是否為模組
b = inspect.ismethod(inspect)     # 檢查inspect是否為物件方法
c = inspect.isfunction(len)       # 檢查len是否為函式
d = inspect.isbuiltin(len)        # 檢查len是否內建函式

e = inspect.getdoc(turtle.circle) # 取得circle的docstring
f = inspect.getsource(turtle)     # 取得指定模組的source code 原始碼

'''

'''
###############################
 利用dict() 函式產生字典物件的方法
###############################
dict(**kwarg)
dict([mapping, **kwarg])  # mapping >> 大括弧 {...}
dict([iterable, **kwarg]) # iterable >> 中括弧 小括弧 可迭代物件 [(xx:xx),(xx:xx)]
'''

