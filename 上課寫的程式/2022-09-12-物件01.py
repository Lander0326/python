
'''

class Demo:
    pass
#print(dir(Demo))
print(Demo.__dict__)
# {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Demo' objects>,
# '__weakref__': <attribute '__weakref__' of 'Demo' objects>, '__doc__': None}

'''

class Demo :
    # def __new__(cls,*args,**kwargs):
    #     super.__new__()
    #     print('__new__')

    def __init__(self,c,d):
        self.a = 100
        self.b = 'Python'
        self.c = c
        self.d = d
        print("__init__")

demo1 = Demo(200,'java')
print(demo1.a)
print(demo1.b)
print(demo1.c)
print(demo1.d)
