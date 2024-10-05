import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("basic-5/3.png", cv2.IMREAD_GRAYSCALE)

h, w = image.shape

n = 10
a = 3
b = 5
N = h

for i in range(n):
    imgr = np.zeros_like(image)  # 创建一个与原图相同大小的空图像

    for y in range(h):
        for x in range(w):
            xx = (a * b + 1) * (x) - b * (y)
            yy = -a * (x) + (y)
            xx = int(xx % N)
            yy = int(yy % N)

            imgr[yy, xx] = image[y, x]  # 使用 W 进行赋值

    image = imgr  # 更新 W 为新的图像

# 显示最终结果
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.show()
