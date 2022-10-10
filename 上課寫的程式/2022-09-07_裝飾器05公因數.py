
import inspect

'''遞迴'''
def gcd1(a: int, b: int) -> int:  # 最大公因數 greatest common divisor，gcd
    if a % b:
        return gcd1(b, a % b)
    else:
        return b

print(gcd1(25,100))

'''多重指派 導讀3.2'''
def gcd2(a: int, b: int) -> int:  # 最大公因數 greatest common divisor，gcd
    while a%b : # a 除以 b 、 如果有餘數就為true 要一直做
        a, b = b, a % b
    return b
print(gcd2(27,36))

'''assert斷言'''
def gcd(a: int, b: int) -> int:
    assert isinstance(a, int), 'Expected int'
    assert isinstance(b, int), 'Expected int'
    while a%b:
        a, b = b, a % b
    return b
# print(gcd(27,36))

a = 10
b = 20

a,b = b,a

print(a,b)