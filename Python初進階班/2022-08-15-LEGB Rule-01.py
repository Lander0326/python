
'''
L :
def square(base):
    result = base ** 2
    print(f'The square of {base} is: {result}')


square(10)

result  # Isn't accessible from outside square()

base  # Isn't accessible from outside square()

square(20)
'''

'''
def outer_func():
    # This block is the Local scope of outer_func()
    var = 100  # A nonlocal var
    # It's also the enclosing scope of inner_func()
    def inner_func():
        # This block is the Local scope of inner_func()
        print(f"Printing var from inner_func(): {var}")

    inner_func()
    print(f"Printing var from outer_func(): {var}")

outer_func()



inner_func()
'''

'''
def outer_func():
    var = 100
    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        print(f"Printing another_var from inner_func(): {another_var}")

    another_var = 200  # This is defined after calling inner_func()
    inner_func()
    print(f"Printing var from outer_func(): {var}")

outer_func()
'''

'''
var = 100  # A global variable
def increment():
    var = var + 1  # Try to update a global variable

increment()
'''
'''
var = 100  # A global variable
def func():
    print(var)  # Reference the global variable, var
    var = 200   # Define a new local variable using the same name, var

func()
'''

var = 10

def func():
    #var = 100  # A nonlocal variable
    def nested():
        #nonlocal var  # Declare var as nonlocal
        #var = 1000
        print(var)
    nested()
    print(var)

func()
print(var)