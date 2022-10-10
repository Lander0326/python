def a1(func):
    def wrapper(*args, **kwargs):
        print('a1-1')
        func(*args, **kwargs)
        print('a1-2')
        return None
    return wrapper

def a2(func):
    def wrapper(*args, **kwargs):
        print('a2-1')
        func(*args, **kwargs)
        print('a2-2')
        return None
    return wrapper

def a3(func):
    def wrapper(*args, **kwargs):
        for item in args:
            print('a3',item)
        func(*args, **kwargs)
        for k, v in kwargs.items():
            print('a3:',k,'a3:',v)
        return None
    return wrapper


@a3
def b(*args, **kwargs):
    for item in args:
        print(item)
    for k,v in kwargs.items():
        print(k,v)
# b = a1( a2( a3( b ) ) )
# b(2,3,a=10,b=10)
b(2,a=20)