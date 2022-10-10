
'''

# i = 5

def f(arg=i):
    print(arg)

i = 6
f()

'''

'''

def f(a, L=[]):
    L.append(a)
    return L

print(f(1,[5,6]))
print(f(2,[7,8]))
print(f(3,[4,5]))

'''

def f(a, L=0):
    L = L+1
    return L

print(f(1))
print(f(2))
print(f(3))
