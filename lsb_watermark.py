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


im = Image.open('img/lena.jpg')
watermark = Image.open('img/tim.jpg')
watermark1 = watermark.convert('L')

code = getcode(watermark1)
encry(im, code)
