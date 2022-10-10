
import re

pattern = re.compile(r'(.*)\.(.*)\.(.*)')
# # pattern = re.compile(r'\d*.?\d*')
# # pattern = re.compile(r"^\d*\.?\d+$")
# pattern = re.compile(r"\d+.+")
a = pattern.findall('32132asd1321.321.')
print(a)
b = pattern.match('100.5..')
print(b)


import re

# def is_number(num):
#     pattern = re.compile(r'(.*)\.(.*)\.(.*)')
#
#     if pattern.match(num):
#         return False
#     return num.replace(".", "").isdigit()
#
# # while True :
# #     num_str = input('請輸入一個浮點數')
# #     if is_number(num_str) :
# #         break
# #     print('重新輸入')
# a = is_number(13.24)
# print(a)
