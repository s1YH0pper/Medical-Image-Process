import numpy as np
import cv2
from matplotlib import pyplot as plt
import time


def files_choice(choice, files_dict):
    im1_file, im2_file, npy_file = files_dict[choice]
    return im1_file, im2_file, npy_file


def image_join(im, x, y, matrix, dimension):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            xy1 = np.array([j - x, i - y, 1])
            xy2 = np.round(matrix @ xy1).astype(int)
            nx, ny = xy2[:2]

            if 0 <= nx < col2 and 0 <= ny < row2:
                if i < y or i >= y + row1 or j < x or j >= x + col1:
                    if dimension == 3:
                        im[i, j, :] = im2[ny, nx, :]
                    else:
                        im[i, j] = im2[ny, nx]
    return im


def imCrop(pic):
    """裁剪函数"""
    if len(pic.shape) == 3:
        gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    else:
        gray = pic

    size = gray.shape[0]
    ceil, bottom, left, right = 0, size - 1, 0, gray.shape[1] - 1

    for k in range(size):
        if np.any(gray[k, :]):
            ceil = k
            break

    for k in range(size - 1, -1, -1):
        if np.any(gray[k, :]):
            bottom = k
            break

    for k in range(gray.shape[1]):
        if np.any(gray[:, k]):
            left = k
            break

    for k in range(gray.shape[1] - 1, -1, -1):
        if np.any(gray[:, k]):
            right = k
            break

    if len(pic.shape) == 3:
        return pic[ceil : bottom + 1, left : right + 1, :]
    else:
        return pic[ceil : bottom + 1, left : right + 1]


file_text = """
选择要处理的图像组:
1: a1.png b1.png d1.npy
2: a2.png b2.png d2.npy
3: a3.jpg b3.jpg d3.npy
"""
choice = int(input(file_text))
files_dict = {
    1: ["a1.png", "b1.png", "d1.npy"],
    2: ["a2.png", "b2.png", "d2.npy"],
    3: ["a3.jpg", "b3.jpg", "d3.npy"],
}
im1_file, im2_file, npy_file = files_choice(choice, files_dict)

# 加载图像
im1 = cv2.imread("advanced-3/" + im1_file)
im2 = cv2.imread("advanced-3/" + im2_file)

# 创建图像布局
fig = plt.figure(figsize=(8, 8))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1])

# 第一张图像 (左上)
ax1 = fig.add_subplot(gs[0, 0])
ax1.imshow(cv2.cvtColor(im1, cv2.COLOR_BGR2RGB))
ax1.set_title("Image 1")
ax1.axis("off")

# 第二张图像 (右上)
ax2 = fig.add_subplot(gs[0, 1])
ax2.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
ax2.set_title("Image 2")
ax2.axis("off")

# 开始计时
start_time = time.time()

# 加载 d1
transfer_mat = np.load("advanced-3/" + npy_file)
size = 3 * max(im1.shape[0], im2.shape[0])

# 判断图像维度
dimension_im = len(im1.shape)
if dimension_im == 3:
    row1, col1, _ = im1.shape
    row2, col2, _ = im2.shape
    im = np.zeros((size, size, 3), dtype=im1.dtype)
else:
    row1, col1 = im1.shape
    row2, col2 = im2.shape
    im = np.zeros((size, size), dtype=im1.dtype)

im_cx = size // 3
im_cy = size // 3

# 将 im1 放置到大图像 im 中心位置
if dimension_im == 3:
    im[im_cy : row1 + im_cy, im_cx : col1 + im_cx, :] = im1
else:
    im[im_cy : row1 + im_cy, im_cx : col1 + im_cx] = im1

# 计算 transfer_mat 的逆矩阵
inv_transfer_mat = np.linalg.inv(transfer_mat)

# 执行图像拼接
im = image_join(im, im_cx, im_cy, inv_transfer_mat, dimension_im)

# 裁剪并转换为 uint8 类型
im = imCrop(im)
im = im.astype(np.uint8)

# 结束计时并打印时间
end_time = time.time()
print("Elapsed time:", end_time - start_time, "seconds")

# 显示结果
ax3 = fig.add_subplot(gs[1, :])
ax3.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
ax3.set_title("Combined Image")
ax3.axis("off")

# 显示排版后的结果
plt.tight_layout()
plt.show()
