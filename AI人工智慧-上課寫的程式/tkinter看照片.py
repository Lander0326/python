import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
import os

root=tk.Tk()
root.title('图片查看器')
root.geometry('1200x800+300+100')

canvas=tk.Canvas(root,height=700,width=1200)
canvas.pack()

path=tk.StringVar()

def resize(image):
    w, h = image.size
    if w > h :
        mlength = w  # 找出最大的边
        mul = 1200 / mlength  # 缩放倍数
    else :
        mlength = h  # 找出最大的边
        mul = 700 / mlength  # 缩放倍数
    w1 = int(w * mul)  # 重新获得高和宽
    h1 = int(h * mul)
    return image.resize((w1, h1))

def show_image(path):
    global img   #要申明全局变量我猜测是调用了canvas
    image = Image.open(path)  # 打开图片
    re_image = resize(image)  # 调用函数
    img = ImageTk.PhotoImage(re_image)  # PhotoImage类是用来在label和canvas展示图片用的
    canvas.create_image(600, 350, anchor=tk.CENTER, image=img)

def openpicture():
#打开一张图片并显示
    global fileindex,fatherpath,files,file_num

    filepath=filedialog.askopenfilename()
    fatherpath=os.path.dirname(filepath)      #获取该路径的上一级路径
    filename=os.path.basename(filepath)   #获取该路径下的文件名
    files=os.listdir(fatherpath)     #该路径下的所有文件并生成列表
    file_num=len(files)
    fileindex=files.index(filename)    #获取当前文件的索引值
    show_image(filepath)


def previous():
    global fileindex, fatherpath, files,file_num
    fileindex -=1
    if fileindex == -1:
        fileindex = file_num-1
    filepath1=os.path.join(fatherpath, files[fileindex])
    show_image(filepath1)

def back():
    global fileindex, fatherpath, files,file_num
    fileindex += 1
    if fileindex == file_num:
        fileindex = 0
    filepath2 = os.path.join(fatherpath, files[fileindex])
    show_image(filepath2)

b=tk.Button(root,text='select a picture',command=openpicture)
b.pack()

b1=tk.Button(root,text='上一张',command=previous).pack(side='left')
b2=tk.Button(root,text='下一张',command=back).pack(side='right')

tk.mainloop()
