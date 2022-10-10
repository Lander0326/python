
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
print(color)


if color == Color.RED :
    print("I see red!")
elif color == Color.GREEN:
    print("Grass is green")
else:
    print("I'm feeling the blues :(")


# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")






'''
def http_error(status):
    match status: # python 3.10後 多重選擇語法
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
'''
