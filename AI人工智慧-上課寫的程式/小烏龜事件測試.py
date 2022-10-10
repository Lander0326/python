from turtle import Turtle, Screen 
from random import random 

def drawing_controls(x, y): 
    pencil.color(random(), random(), random()) 
    square.color(*pencil.color()) 

def drag_pencil(x, y): 
    pencil.ondrag(None) 
    pencil.goto(x, y) 
    pencil.ondrag(drag_pencil) 

square = Turtle('square', visible=False) 
square.speed('fastest') 
square.hideturtle() 
square.up() 

square.goto(-200, 230) 
square.write('Change Color', align='center') 

square.goto(-200, 200) 
square.shapesize(50/20) 
square.showturtle() 

pencil = Turtle('circle') 

square.onclick(drawing_controls) 

pencil.ondrag(drag_pencil) 

window = Screen() 
window.mainloop() 
