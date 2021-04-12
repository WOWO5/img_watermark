# LSB算法实现数字水印
from PIL import Image

def plus(str):
    return str.zfill(8)  # 指定字符串的长度，长度不够用0在前面补充


# 获取水印图像的像素值序列
def getcode(watermark):
    the_str = ''
    # 获取水印图片的每一个像素值,i：指定要检查的像素点的逻辑X轴坐标。j：指定要检查的像素点的逻辑Y轴坐标。
    for i in range(watermark.size[0]):
        for j in range(watermark.size[1]):
            # 获取每个像素的RGB值
            num_L = watermark.getpixel((i, j))
            the_str += plus(bin(num_L).replace('0b', ''))
    return the_str

# 水印嵌入
def encry(img, code):
    count = 0  # 计数器
    codelen = len(code)
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
    img.save('img/watermark_img.png')
    return img


# 提取水印图像的像素值序列
def deEncry(img, length):
    width = img.size[0]
    height = img.size[1]
    count = 0  # 计数器
    wt = ''

    for i in range(width):
        for j in range(height):
            # 获取像素点的值
            rgb = img.getpixel((i, j))
            # 提取R通道的附加值
            if count % 3 == 0:
                count += 1
                wt = wt + str(rgb[0] % 2)
                if count == length: break

            # 提取G通道的附加值
            if count % 3 == 1:
                count += 1
                wt = wt + str(rgb[1] % 2)
                if count == length: break

            # 提取B通道的附加值
            if count % 3 == 2:
                count += 1
                wt = wt + str(rgb[2] % 2)
                if count == length: break

        if count == length: break
    return wt


# 将水印图像的像素值序列显示为图片
def showImage(wt):
    str_decode = []
    for i in range(0, len(wt), 8):
        str_decode.append(int(wt[i:i + 8], 2))  # 将二进制序列转换为十进制
    img_out = Image.new("L", (32, 32))
    flag = 0
    for m in range(0, 32):
        for n in range(0, 32):
            img_out.putpixel((m, n), str_decode[flag])
            flag += 1
    img_out.save('img/water_img.png')
