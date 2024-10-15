import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转换为灰度图像
I = cv2.imread("basic-8/2.jpg")
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# 显示灰度图像
plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.imshow(I_gray, cmap="gray")
plt.title("Gray Image")

# 使用 np.digitize 来模拟 grayslice 分割灰度图像为 16 个级别
levels = 16
bins = np.linspace(0, 255, levels + 1)  # 创建分割区间
G2C = np.digitize(I_gray, bins) - 1  # 对灰度图像进行分级

# 使用 OpenCV 的 applyColorMap 来实现伪彩色映射
# 定义伪彩色映射方案，例如使用 JET 颜色映射
pseudo_colored = cv2.applyColorMap(
    (G2C * (255 // levels)).astype(np.uint8), cv2.COLORMAP_JET
)

# 显示伪彩色图像
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(pseudo_colored, cv2.COLOR_BGR2RGB))  # 转换为RGB显示
plt.title("Pseudo-color Image\nwith JET colormap")
plt.colorbar()  # 显示颜色条

# 显示图像
plt.show()
