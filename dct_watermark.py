import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def the_dct(water_img):

    count = 0
    A, count1, count2, si, ti = 0.01, 0, 1, [128, 128], [0, 0]
    img_gray = cv2.imread('img/lena.png', cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图像
    height, width = img_gray.shape  # 获得图像的长和宽

    dct_coeff = np.zeros((height, width), dtype=np.float32)  # 建立原始矩阵
    N = 8  # 块大小

    for row in np.arange(0, height, N):
        for col in np.arange(0, width, N):
            block = np.array(img_gray[row:(row+N), col:(col+N)], dtype=np.float32)  # 每一块的矩阵值
            water_block = np.zeros((8, 8), dtype=np.float32)
            if row == si[0] and col == si[1]:
                water_block = np.array(water_img[ti[0]:(ti[0]+N), ti[1]:(ti[1]+N)], dtype=np.float32)
                count1 += 1
                if count1 == 4 and count2 < 4:
                    si[0] = si[0] + N
                    si[1] = si[1] - N*4
                    ti[0] = ti[0] + N
                    ti[1] = ti[1] - N*4
                    count1, count2 = 0, count2+1
                si[1] = si[1]+N
                ti[1] = ti[1]+N
                if count2 == 4 and count1 == 4:
                    si[1] = si[1]-2*N
                    ti[1] = ti[1]-2*N
                count += 1
            water_dct = cv2.dct(water_block)
            original_dct = cv2.dct(block)
            result_dct = original_dct + water_block * A
            dct_coeff[row:(row+N), col:(col+N)] = result_dct  # 每一块进行dct变换并赋给原图像

    idct_coeff = dct_coeff
    dct_coeff = np.abs(dct_coeff)
    dct_coeff = np.array(255*(dct_coeff/np.max(dct_coeff)), np.uint8)

    for row in np.arange(0, height, N):
        for col in np.arange(0, width, N):
            block = np.array(idct_coeff[row:(row+N), col:(col+N)], dtype=np.float32)
            idct_coeff[row:(row+N), col:(col+N)] = cv2.idct(block)

    cv2.imwrite('img/watermark_img.png', idct_coeff)


def the_idct():

    A = 0.01
    si, ti = [128, 128], [0, 0]
    count, count1, count2 = 0, 0, 1
    # 读取原图像和添加水印后的图像
    img_gray1 = cv2.imread('img/lena.png', cv2.IMREAD_GRAYSCALE)
    img_gray2 = cv2.imread('img/watermark_img.png', cv2.IMREAD_GRAYSCALE)
    height, width = img_gray1.shape

    dct_coeff = np.zeros((height, width), dtype=np.float32)
    waterImg = np.zeros((32, 32), dtype=np.float32)
    N = 8

    for row in np.arange(0, height, N):
        for col in np.arange(0, width, N):
            block1 = np.array(img_gray1[row:(row+N), col:(col+N)], dtype=np.float32)
            block2 = np.array(img_gray2[row:(row+N), col:(col+N)], dtype=np.float32)  # 每一块的矩阵值
            if row == si[0] and col == si[1]:
                original_dct1 = cv2.dct(block1)
                original_dct2 = cv2.dct(block2)
                original_dct1 = original_dct1/A
                original_dct2 = original_dct2/A
                block = original_dct2 - original_dct1
                waterImg[ti[0]:(ti[0]+N), ti[1]:(ti[1]+N)] = block
                count1 += 1
                if count1 == 4 and count2 < 4:
                    si[0] = si[0] + N
                    si[1] = si[1] - N*4
                    ti[0] = ti[0] + N
                    ti[1] = ti[1] - N*4
                    count1, count2 = 0, count2+1
                si[1] = si[1]+N
                ti[1] = ti[1]+N
                if count2 == 4 and count1 == 4:
                    si[1] = si[1]-2*N
                    ti[1] = ti[1]-2*N
                count += 1
    cv2.imwrite('img/water_img.png', waterImg)
