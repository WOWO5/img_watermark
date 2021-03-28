from tkinter import *
from tkinter.ttk import Separator
import time

the_algorithm = 0

root = Tk()
root.title('数字水印')

# 设置窗口大小
width = 500
height = 300
x = width * 0.2
y = height * 0.2
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.maxsize(width, height)  # 窗口最大值
root.minsize(width, height)  # 窗口最小值

# 设置颜色，图标
root.configure(bg="#87CEEB")
root.iconbitmap("icon/orange.ico")


# 弹窗选择函数
def open_LSB():
    root_LSB = Toplevel()
    root_LSB.title('算法选择')
    root_LSB.geometry('300x300')
    root_LSB.configure(bg="#87CEEB")
    root_LSB.iconbitmap('icon/apple.ico')

    def chose1():
        global the_algorithm
        the_algorithm = 1
        labe1_text['text'] = 'LSB算法'
        labe1_text['fg'] = 'green'

    def chose2():
        global the_algorithm
        the_algorithm = 2
        labe1_text['text'] = 'DCT算法'
        labe1_text['fg'] = 'green'

    def chose3():
        global the_algorithm
        the_algorithm = 3
        labe1_text['text'] = '傅里叶变换'
        labe1_text['fg'] = 'green'

    btn1 = Button(root_LSB, text='LSB算法', width=20, command=chose1)
    btn2 = Button(root_LSB, text='DCT算法', width=20, command=chose2)
    btn3 = Button(root_LSB, text='傅里叶变换', width=20, command=chose3)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    root_LSB.mainloop()


def open_DCT():
    root_DCT = Toplevel()
    root_DCT.title('水印选择')
    root_DCT.geometry('300x300')
    root_DCT.configure(bg="#87CEEB")
    root_DCT.iconbitmap('icon/lemon.ico')

    btn1 = Button(root_DCT, text='图像1', width=20)
    btn2 = Button(root_DCT, text='图像2', width=20)
    btn3 = Button(root_DCT, text='图像3', width=20)
    btn1.pack()
    btn2.pack()
    btn3.pack()

    root_DCT.mainloop()


# 设置主界面控件

label1 = Label(root, text='原始图像->', font=30, width=10)
label1.place(x=0, y=140)
original_img = PhotoImage(file='img/lena.png')
label2 = Label(root, image=original_img)
label2.place(x=110, y=50)
labe1_text = Label(root, text='暂未选择算法', font=10, width=15, fg='red', bg="#87CEEB")
labe1_text.place(x=350, y=0)
button1 = Button(root, text='请选择使用算法', command=open_LSB)
button1.place(x=330, y=110)
button2 = Button(root, text='请选择水印图像', command=open_DCT)
button2.place(x=330, y=160)
root.mainloop()
