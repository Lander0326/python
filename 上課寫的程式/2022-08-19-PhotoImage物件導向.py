
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')
        self.geometry('520x1040')

        self.image1 = Image.open('Mario_Galaxy_001.jpg')
        self.image2 = Image.open('Mario_Galaxy_002.jpg')
        self.python_image1 = ImageTk.PhotoImage(self.image1)
        self.python_image2 = ImageTk.PhotoImage(self.image2)

        # self.python_image = tk.PhotoImage(file='Mario_Galaxy_002.png')

        ttk.Label(self, image=self.python_image1).pack()
        ttk.Label(self, image=self.python_image2).pack()

# 錯誤 : 因為沒有寫self
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         python_image = tk.PhotoImage(file='./assets/python.png')
#         ttk.Label(self, image=python_image).pack()



if __name__ == '__main__':
    obj1 = App()
    obj1.mainloop()
