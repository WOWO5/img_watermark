from PIL import Image

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

def showImage(wt):
    str_decode = []
    for i in range(0, len(wt), 8):
        str_decode.append(int(wt[i:i + 8], 2))
    img_out = Image.new("L", (200, 200))
    flag = 0
    for m in range(0, 200):
        for n in range(0, 200):
            img_out.putpixel((m, n), str_decode[flag])
            flag += 1
    img_out.show()

img = Image.open('watermark_img.png')
img_rgb = img.convert('RGB')
length = 320000
wt = deEncry(img_rgb, length)
showImage(wt)
