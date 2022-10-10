from tkinter import *

canvas_width =  1200
canvas_height = 800

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="STScI-01G8GZQ3ZFJRD8YF8YZWMAXCE3.png")
canvas.create_image(20,20, anchor=NW, image=img) # img指上面那行的img

mainloop()