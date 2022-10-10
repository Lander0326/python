
def fib(n):    # write Fibonacci series up to n 費氏數列
    """Print a Fibonacci series up to n.
       這是費氏係數的函式"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    return None
# Now call the function we just defined:
fib(2000)