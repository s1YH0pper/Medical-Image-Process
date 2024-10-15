import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("basic-8/1.jpg")

# 显示原始图像
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# 转换为灰度图像
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(1, 3, 2)
plt.imshow(image_gray, cmap="gray")
plt.title("Gray Image")

# 获取图像的高度和宽度
h, w = image_gray.shape
L = 255

# 预定义伪彩色通道
r = np.zeros_like(image_gray, dtype=np.uint8)
g = np.zeros_like(image_gray, dtype=np.uint8)
b = np.zeros_like(image_gray, dtype=np.uint8)

# 使用条件索引映射
r = np.where(
    image_gray <= L / 4,
    0,
    np.where(
        image_gray <= L / 2,
        0,
        np.where(image_gray <= 3 * L / 4, 4 * image_gray - 2 * L, L),
    ),
)
g = np.where(
    image_gray <= L / 4,
    4 * image_gray,
    np.where(
        image_gray <= L / 2,
        L,
        np.where(image_gray <= 3 * L / 4, L, -4 * image_gray + 4 * L),
    ),
)
b = np.where(
    image_gray <= L / 4, L, np.where(image_gray <= L / 2, -4 * image_gray + 2 * L, 0)
)

# 合并 R, G, B 通道形成伪彩色图像
rgbim = np.stack([r, g, b], axis=-1)

# 归一化到0-1范围（Matplotlib需要）
rgbim = rgbim / 255.0

# 显示伪彩图像
plt.subplot(1, 3, 3)
plt.imshow(rgbim)
plt.title("Pseudo-color Image")

plt.show()
