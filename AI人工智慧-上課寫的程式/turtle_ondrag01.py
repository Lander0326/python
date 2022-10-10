
from turtle import Screen, Turtle

screen = Screen()
t = Turtle('square')
t.speed(0)                          

def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight(x,y):
    t.clear()

def main():  # This will run the program

    #screen.listen()
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    screen.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()
