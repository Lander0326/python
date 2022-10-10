# ch11_31.py
# 使用一般函數
# def square(x):
#     value = x ** 2
#     return value
#
# 輸出平方值
# print(square(10))

''''''

# ch11_32.py
# 定義lambda函數
# square = lambda x : x ** 2 # 函式 指派 給 S變數 >> 改名
#
# 輸出平方值
# print(square(10)) # 由變數呼叫函式(匿名函式)

''''''

# ch11_33.py
# 定義lambda函數
# product = lambda x, y: x * y
#
# 輸出相乘結果
# print(product(5, 10))

''''''

# ch11_33_1.py
# def func(b):
#     return lambda x : 2 * x + b
#
# linear  = func(5)       # 5 將傳給lambda的 b >> 2 * x  + 5
# 相當於以下
# linear(x):
#   return 2 * x + 5
#
# print(linear(10))       # 10 是lambda的 x   +>> 2 * 10 + 5

''''''

# ch11_33_2.py
# def func(b):
#     return lambda x : 2 * x + b
#
# linear  = func(5)       # 5將傳給lambda的 b
# print(linear(10))       # 10是lambda的 x
#
# linear2 = func(3)
# print(linear2(10))

''''''

''' 閉包 '''
#
# def power_factory(exp):
#     def power(base):
#         return base ** exp
#     return power
#
# square = power_factory(2)
# print(square(10))
#
# cube = power_factory(3)
# print(cube(10))
#
# print(cube(5))
#
# print(square(15))

''''''

def mean():
    sample = []
    def _mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return _mean

current_mean = mean()
current_mean(10)

current_mean(15)

current_mean(12)

current_mean(11)

current_mean(13)