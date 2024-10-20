import cv2
import numpy as np
import matplotlib.pyplot as plt


# 定义函数用于读取并转换图像为灰度图
def load_and_convert_to_gray(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Unable to load image at path: {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


print("选择要处理的图像:")
print("1: 颅脑横断面图像")
print("2: 颈椎矢状面图像")

choice = input("请输入对应的数字(1-2): ")

if choice == "1":
    img_path = "advanced-7/1.png"
elif choice == "2":
    img_path = "advanced-7/2.png"
else:
    print("无效选择，请重新运行程序。")
    exit()

# 尝试加载图像
try:
    img = load_and_convert_to_gray(img_path)
except FileNotFoundError as e:
    print(e)
    exit()

plt.figure(figsize=(9, 7))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")

flot_gray_img = img.astype(np.float64)
h, w = flot_gray_img.shape

# 对数变换
f = 20 * np.log(flot_gray_img + 1)
plt.subplot(2, 3, 2)
plt.imshow(np.uint8(f), cmap="gray")
plt.title("Log Transformation")

# 分段线性变换
x0, y0 = 0, 0
x1, y1 = 20, 55
x2, y2 = 221, 180
x3, y3 = 255, 255

plt.subplot(2, 3, 3)
plt.plot([x0, x1, x2, x3], [y0, y1, y2, y3])
plt.title("Piecewise Linear\nTransformation Function")
plt.xlim(0, 255)
plt.ylim(0, 255)

# 计算分段线性函数的斜率和截距
r1 = (y1 - y0) / (x1 - x0)
i1 = -r1 * x0 + y0
r2 = (y2 - y1) / (x2 - x1)
i2 = -r2 * x1 + y1
r3 = (y3 - y2) / (x3 - x2)
i3 = -r3 * x2 + y2

# 分段线性变换
u = np.zeros_like(flot_gray_img)

for i in range(h):
    for j in range(w):
        t = flot_gray_img[i, j]
        if x0 <= t <= x1:
            u[i, j] = r1 * t + i1
        elif x1 < t <= x2:
            u[i, j] = r2 * t + i2
        elif x2 < t <= x3:
            u[i, j] = r3 * t + i3

plt.subplot(2, 3, 4)
plt.imshow(u, cmap="gray")
plt.title("Piecewise Linear\nTransformed Image")

# 图像取反
flot_gray_img_inv = 255 - flot_gray_img
plt.subplot(2, 3, 5)
plt.imshow(np.uint8(flot_gray_img_inv), cmap="gray")
plt.title("Inverted Image")

# 直方图均衡化
h_equa_img = cv2.equalizeHist(img)

plt.figure(figsize=(7, 7))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(h_equa_img, cmap="gray")
plt.title("Histogram Equalized Image")

plt.subplot(2, 2, 3)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Original Image Histogram")

plt.subplot(2, 2, 4)
plt.hist(h_equa_img.ravel(), 256, [0, 256])
plt.title("Histogram Equalized Histogram")

plt.tight_layout()
plt.show()
