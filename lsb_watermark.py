# LSB算法实现数字水印
from PIL import Image

def plus(str):
    return str.zfill(8)  # 指定字符串的长度，长度不够用0在前面补充

def getcode(watermark):
    the_str = ''
    # 获取水印图片的每一个像素值,i：指定要检查的像素点的逻辑X轴坐标。j：指定要检查的像素点的逻辑Y轴坐标。
    for i in range(watermark.size[0]):
        for j in range(watermark.size[1]):
            # 获取每个像素的RGB值
            num_L = watermark.getpixel((i, j))
            the_str += plus(bin(num_L).replace('0b', ''))
    return the_str

# 加密

def encry(img, code):
    count = 0  # 计数器
    codelen = len(code)
    print(codelen)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # 获取每个像素的RGB值
            data = img.getpixel((i,j))
            if count == codelen: break
            r = data[0]
            g = data[1]
            b = data[2]
            r = (r - r % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            g = (g - g % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            b = (b - b % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            if count % 3 == 0:
                img.putpixel((i, j), (r, g, b))
    img.show()
    img.save('watermark_img.png')


im = Image.open('lena.jpg')
watermark = Image.open('tim.jpg')
watermark1 = watermark.convert('L')

code = getcode(watermark1)
encry(im, code)






'''

    获取灰度图像

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    # 显示图片
    width, height = im.size  # 获取图像的宽高
    im = im.convert("L")  # 转换为灰度图像
    data = im.getdata()  # 返回图像的数值数据
    data = np.matrix(data, dtype='float') / 255.0  # 生成矩阵
    new_data = np.reshape(data, (height, width))  # 用获取到的宽高来修改矩阵形状
    return new_data

def MatrixToImage(data):
    data = data * 255
    new_im = Image.fromarray(data.astype(np.uint8))  # 数据矩阵值 --> 图像
    return new_im


filename = 'tim.jpg'
data = ImageToMatrix(filename)
print(data)
new_im = MatrixToImage(data)
plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save('tim_1.jpg')

'''


