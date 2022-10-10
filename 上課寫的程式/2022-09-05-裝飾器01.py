value = 3
print(type(value))

value = [1,2,3]
print(type(value))

def demo(para) :
    print(type(para))

demo(3)
demo([1,2,3])

def demo1( para1:int , para2:str ) -> str :
    return para2*para1
# ans = demo1([1,2,3],3)
# print(ans)
# ans = demo1(3,5)
# print(ans)

print(demo1.__annotations__) # {'para1': <class 'int'>, 'para2': <class 'str'>, 'return': <class 'str'>}

def demo2(v1:int,v2:3,v3:'5')->6 :
    return (v1,v2,v3)

print(demo2(1,2,3))
print(demo2.__annotations__)

# __name__,__module__,__annotations__,__kwdefaults__,__defaults__ 去查用法

def demo3(a:3 , b:5) -> int :
    c:6
    d:8
    return sum((a,b,c,d))
# demo3(1,2)
print(demo3.__annotations__)

'''
e : 9
f : list
g : 'Beautiful is better than ugly'
只是註解而已
print(__annotations__) # {'e': 9, 'f': <class 'list'>, 'g': 'Beautiful is better than ugly'}
print(e,f,g)  # NameError e, f, g 還沒定義
'''
name : '姓名'
age : '年齡'
sex : '性別' # 45-47 都是註解 電腦也可接受

print(__annotations__)