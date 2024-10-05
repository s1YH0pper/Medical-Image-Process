import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像和水印图像
image = cv2.imread("basic-5/1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("basic-5/2.jpg", cv2.IMREAD_GRAYSCALE)

# 调整图像大小
M = 1600
N = 200
K = 8
image = cv2.resize(image, (M, M))
image2 = cv2.resize(image2, (N, N))
_, image2 = cv2.threshold(image2, 0.65 * 255, 255, cv2.THRESH_BINARY)

# 显示原始图像和水印图像
plt.figure(figsize=(8, 5))
plt.subplot(2, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.subplot(2, 3, 2)
plt.imshow(image2, cmap="gray")
plt.title("Watermark Image")

# 获取水印图像的尺寸
h, w = image2.shape

# 置乱参数
n = 10
a = 3
b = 5
N = h
A = image.copy()

# 置乱水印图像
for i in range(n):
    imgn = np.zeros((h, w), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            xx = (x + b * y) % N
            yy = (a * x + (a * b + 1) * y) % N
            imgn[yy, xx] = image2[y, x]
    image2 = imgn

# 显示置乱后的水印图像
plt.subplot(2, 3, 3)
plt.imshow(image2, cmap="gray")
plt.title("Scramble Image")

# DCI水印嵌入和提取参数
K = 8
alpha = 0.03
watermark_img = np.zeros((N, N), dtype=np.uint8)

# 水印嵌入算法
for p in range(N):
    for q in range(N):
        x = p * K
        y = q * K
        BLOCK = image[x : x + K, y : y + K].astype(np.float32)
        BLOCK = cv2.dct(BLOCK)
        a = -1 if image2[p, q] == 0 else 1
        BLOCK = BLOCK * (1 + a * alpha)
        BLOCK = cv2.idct(BLOCK)
        image[x : x + K, y : y + K] = BLOCK

# 显示嵌入水印后的图像
plt.subplot(2, 3, 4)
plt.imshow(image, cmap="gray")
plt.title("Encryption Image")

# 提取水印
image2 = image.copy()
image = A.copy()

for p in range(N):
    for q in range(N):
        x = p * K
        y = q * K
        BLOCK1 = image[x : x + K, y : y + K].astype(np.float32)
        BLOCK2 = image2[x : x + K, y : y + K].astype(np.float32)
        if BLOCK1[0, 0] != 0:
            a = BLOCK2[0, 0] / BLOCK1[0, 0] - 1
            watermark_img[p, q] = 0 if a < 0 else 1

# 显示提取的水印
plt.subplot(2, 3, 5)
plt.imshow(watermark_img, cmap="gray")
plt.title("From the extracted watermark Image")

# 水印图像复原
n = 10
a = 3
b = 5

for i in range(n):
    imgr = np.zeros((h, w), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            xx = ((a * b + 1) * x - b * y) % N
            yy = (-a * x + y) % N
            imgr[yy, xx] = watermark_img[y, x]
    watermark_img = imgr

# 显示复原的水印图像
plt.subplot(2, 3, 6)
plt.imshow(watermark_img, cmap="gray")
plt.title("Original Image")

plt.tight_layout()
plt.show()
