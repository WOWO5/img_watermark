import cv2
import numpy as np
import random
ALPHA = 5

def encode(img_path, wm_path, res_path, alpha):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_f = np.fft.fft2(img)
    height, width = np.shape(img)
    watermark = cv2.imread(wm_path, cv2.IMREAD_GRAYSCALE)
    wm_height, wm_width = watermark.shape[0], watermark.shape[1]
    x, y = list(range(height // 2)), list(range(width))
    random.seed(height + width)
    random.shuffle(x)
    random.shuffle(y)
    tmp = np.zeros(img.shape)
    for i in range(height // 2):
        for j in range(width):
            if x[i] < wm_height and y[j] < wm_width:
                tmp[i][j] = watermark[x[i]][y[j]]
                tmp[height - 1 - i][width - 1 - j] = tmp[i][j]
    res_f = img_f + alpha * tmp
    res = np.fft.ifft2(res_f)
    res = np.real(res)
    cv2.imwrite(res_path, res)


def decode(ori_path, img_path, res_path, alpha):
    ori = cv2.imread(ori_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ori_f = np.fft.fft2(ori)
    img_f = np.fft.fft2(img)
    height, width = ori.shape[0], ori.shape[1]
    watermark = (ori_f - img_f) / alpha
    watermark = np.real(watermark)
    res = np.zeros(watermark.shape)
    random.seed(height + width)
    x = list(range(height // 2))
    y = list(range(width))
    random.shuffle(x)
    random.shuffle(y)
    for i in range(height // 2):
        for j in range(width):
            res[x[i]][y[j]] = watermark[i][j]
    cv2.imwrite(res_path, res)
