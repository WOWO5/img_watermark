from tkinter import *
import cv2
from tkinter.messagebox import *
from PIL import Image
import lsb_watermark as lsb
import dct_watermark as dct
import fft_watermark as fft

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
    root_LSB.geometry('300x230')
    root_LSB.configure(bg="#87CEEB")
    root_LSB.iconbitmap('icon/apple.ico')
    root_LSB.maxsize(300, 230)
    root_LSB.minsize(300, 230)

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
    btn1.place(x=80, y=30)
    btn2.place(x=80, y=90)
    btn3.place(x=80, y=150)
    root_LSB.mainloop()

# 选择水印图像
def open_DCT():
    root_DCT = Toplevel()
    root_DCT.title('水印选择')
    root_DCT.geometry('300x230')
    root_DCT.configure(bg="#87CEEB")
    root_DCT.iconbitmap('icon/lemon.ico')
    root_DCT.maxsize(300, 230)  # 窗口最大值
    root_DCT.minsize(300, 230)  # 窗口最小值

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
    btn1.place(x=130, y=40)
    btn2.place(x=130, y=100)
    btn3.place(x=130, y=160)
    img1 = PhotoImage(file='img/tim.png')
    img2 = PhotoImage(file='img/astronaut.png')
    img3 = PhotoImage(file='img/meteor.png')
    lab1 = Label(root_DCT, image=img1)
    lab2 = Label(root_DCT, image=img2)
    lab3 = Label(root_DCT, image=img3)
    lab1.place(x=50, y=35)
    lab2.place(x=50, y=95)
    lab3.place(x=50, y=155)

    root_DCT.mainloop()


# 水印嵌入算法选择
def start_work():

    cho1 = 'img/tim.png'  # 水印图片路径
    cho2 = 'img/astronaut.png'
    cho3 = 'img/meteor.png'
    cho = ''
    if the_waterImg == 1:
        cho = cho1
    elif the_waterImg == 2:
        cho = cho2
    elif the_waterImg == 3:
        cho = cho3
    else:
        showwarning('警告', '请选择水印图片！')

    im = Image.open('img/lena.png')
    watermark = Image.open(cho)
    watermark1 = watermark.convert('L')
    if the_algorithm == 1:
        code = lsb.getcode(watermark1)
        lsb.encry(im, code)
        global watermark_img
        watermark_img = PhotoImage(file=localLoad_mark)
        showImg1()
    elif the_algorithm == 2:
        water_img = cv2.imread(cho, cv2.IMREAD_GRAYSCALE)  # 水印图像
        dct.the_dct(water_img)
        watermark_img = PhotoImage(file=localLoad_mark)
        showImg1()
    elif the_algorithm == 3:
        fft.encode('img/lena.png', cho, 'img/watermark_img.png', fft.ALPHA)
        watermark_img = PhotoImage(file=localLoad_mark)
        showImg1()
    else:
        showwarning('警告', '请选择使用算法！')


def showImg1():
    label4['image'] = watermark_img

# 水印提取算法选择
def pickUp_img():
    img = Image.open('img/watermark_img.png')
    if the_algorithm == 1:
        img_rgb = img.convert('RGB')
        length = 115200
        wt = lsb.deEncry(img_rgb, length)
        lsb.showImage(wt)
    elif the_algorithm == 2:
        dct.the_idct()
    elif the_algorithm == 3:
        fft.decode('img/watermark_img.png', 'img/lena.png', 'img/water_img.png', fft.ALPHA)
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
label2.place(x=55, y=90)

label3 = Label(root, text='含水印图像', font=20, width=15)  # 含水印图像显示
label3.place(x=450, y=50)
false_img = PhotoImage(file='img/false-img.png')
label4 = Label(root, image=false_img)
label4.place(x=400, y=90)

label5 = Label(root, text='提取水印图像', font=20, width=15)  # 水印图像显示
label5.place(x=800, y=50)
label6 = Label(root, image=false_img)
label6.place(x=760, y=90)

# 警告信息
label1_text = Label(root, text='暂未选择水印算法', font='light 10 normal', width=15, fg='blue', bg="#87CEEB", anchor=W)
label1_text.place(x=-1, y=0)
label2_text = Label(root, text='暂未选择水印图像', font='light 10 normal', width=15, fg='blue', bg='#87CEEB', anchor=W)
label2_text.place(x=-1, y=20)


# 功能选择按钮
button1 = Button(root, text='选择水印算法', command=open_LSB, width=12)
button1.place(x=20, y=360)
button2 = Button(root, text='选择水印图像', command=open_DCT, width=12)
button2.place(x=130, y=360)
button3 = Button(root, text='嵌入水印', command=start_work, width=12)
button3.place(x=250, y=360)
button4 = Button(root, text='提取水印', command=pickUp_img, width=12)
button4.place(x=360, y=360)

root.mainloop()
