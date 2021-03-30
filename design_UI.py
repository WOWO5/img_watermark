from tkinter import *
from tkinter.ttk import Separator
from PIL import Image
import time
import lsb_watermark as lsb

the_algorithm = 0
the_waterImg = 0
watermark_img = ''
water_img = ''
localLoad_mark = 'img/watermark_img.png'
localLoad_water = 'img/water_img.png'

root = Tk()  # 新建窗口
root.title('数字水印')

# 设置窗口大小
width = 1050
height = 500
x = width * 0.2  # 窗口起始位置
y = height * 0.2
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.maxsize(width, height)  # 窗口最大值
root.minsize(width, height)  # 窗口最小值

# 设置颜色，图标
root.configure(bg="#87CEEB")
root.iconbitmap("icon/orange.ico")


# 选择算法
def open_LSB():
    root_LSB = Toplevel()
    root_LSB.title('算法选择')
    root_LSB.geometry('300x300')
    root_LSB.configure(bg="#87CEEB")
    root_LSB.iconbitmap('icon/apple.ico')

    def chose1():
        global the_algorithm
        the_algorithm = 1
        label1_text['text'] = 'LSB算法'
        label1_text['fg'] = 'green'

    def chose2():
        global the_algorithm
        the_algorithm = 2
        label1_text['text'] = 'DCT算法'
        label1_text['fg'] = 'green'

    def chose3():
        global the_algorithm
        the_algorithm = 3
        label1_text['text'] = '傅里叶变换'
        label1_text['fg'] = 'green'

    btn1 = Button(root_LSB, text='LSB算法', width=20, command=chose1)
    btn2 = Button(root_LSB, text='DCT算法', width=20, command=chose2)
    btn3 = Button(root_LSB, text='傅里叶变换', width=20, command=chose3)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    root_LSB.mainloop()

# 选择水印图像
def open_DCT():
    root_DCT = Toplevel()
    root_DCT.title('水印选择')
    root_DCT.geometry('300x300')
    root_DCT.configure(bg="#87CEEB")
    root_DCT.iconbitmap('icon/lemon.ico')

    def chose1():
        global the_waterImg
        the_waterImg = 1
        label2_text['text'] = '图像1'
        label2_text['fg'] = 'green'

    def chose2():
        global the_waterImg
        the_waterImg = 2
        label2_text['text'] = '图像2'
        label2_text['fg'] = 'green'

    def chose3():
        global the_waterImg
        the_waterImg = 3
        label2_text['text'] = '图像3'
        label2_text['fg'] = 'green'

    btn1 = Button(root_DCT, text='图像1', width=20, command=chose1)
    btn2 = Button(root_DCT, text='图像2', width=20, command=chose2)
    btn3 = Button(root_DCT, text='图像3', width=20, command=chose3)
    btn1.pack()
    btn2.pack()
    btn3.pack()

    root_DCT.mainloop()


# 水印嵌入算法选择
def start_work():
    im = Image.open('img/lena.png')
    watermark = Image.open('img/tim.png')
    watermark1 = watermark.convert('L')
    code = lsb.getcode(watermark1)
    lsb.encry(im, code)
    global watermark_img
    watermark_img = PhotoImage(file=localLoad_mark)
    showImg1()

def showImg1():
    label4['image'] = watermark_img

# 水印提取算法选择
def pickUp_img():
    img = Image.open('img/watermark_img.png')
    img_rgb = img.convert('RGB')
    length = 115200
    wt = lsb.deEncry(img_rgb, length)
    lsb.showImage(wt)
    global water_img
    water_img = PhotoImage(file=localLoad_water)
    showImg2()

def showImg2():
    label6['image'] = water_img

# 设置主界面控件


label1 = Label(root, text='原始图像', font=30, width=10)  # 原始图像显示
label1.place(x=130, y=50)
original_img = PhotoImage(file='img/lena.png')
label2 = Label(root, image=original_img)
label2.place(x=80, y=100)

label3 = Label(root, text='含水印图像', font=20, width=15)  # 含水印图像显示
label3.place(x=450, y=50)
false_img = PhotoImage(file='img/false-img.png')
label4 = Label(root, image=false_img)
label4.place(x=420, y=100)

label5 = Label(root, text='提取水印图像', font=20, width=15)  # 水印图像显示
label5.place(x=800, y=50)
label6 = Label(root, image=false_img)
label6.place(x=780, y=100)

# 警告信息
label1_text = Label(root, text='暂未选择水印算法', font='light 10 normal', width=15, fg='blue', bg="#87CEEB", anchor=W)
label1_text.place(x=-1, y=0)
label2_text = Label(root, text='暂未选择水印图像', font='light 10 normal', width=15, fg='blue', bg='#87CEEB', anchor=W)
label2_text.place(x=-1, y=20)


# 功能选择按钮
button1 = Button(root, text='选择水印算法', command=open_LSB, width=12)
button1.place(x=20, y=320)
button2 = Button(root, text='选择水印图像', command=open_DCT, width=12)
button2.place(x=130, y=320)
button3 = Button(root, text='嵌入水印', command=start_work, width=12)
button3.place(x=250, y=320)
button4 = Button(root, text='提取水印', command=pickUp_img, width=12)
button4.place(x=360, y=320)


root.mainloop()



