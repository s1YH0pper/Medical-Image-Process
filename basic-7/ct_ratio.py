import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg


def calculate_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# 读取图像
img = mpimg.imread("basic-7/1.jpg")

# 定义点坐标
points = {
    "P1": (278, 99),
    "P2": (278, 420),
    "P3": (377, 385),
    "P4": (278, 385),
    "P5": (220, 370),
    "P6": (278, 370),
    "P7": (51, 473),
    "P8": (493, 473),
}

# 绘制图像
fig, ax = plt.subplots()
ax.imshow(img)

# 绘制线段
lines = [
    {"start": "P1", "end": "P2", "color": "black", "label": None},
    {"start": "P3", "end": "P4", "color": "blue", "label": "b"},
    {"start": "P5", "end": "P6", "color": "green", "label": "a"},
    {"start": "P7", "end": "P8", "color": "red", "label": "c"},
]

for line in lines:
    start = points[line["start"]]
    end = points[line["end"]]
    ax.plot([start[0], end[0]], [start[1], end[1]], color=line["color"], linewidth=2)
    if line["label"]:
        text_x = (start[0] + end[0]) / 2
        text_y = (start[1] + end[1]) / 2 - 15
        ax.text(text_x, text_y, line["label"], fontsize=12, color=line["color"])


# 计算线段长度
a = calculate_distance(points["P3"], points["P4"])
b = calculate_distance(points["P5"], points["P6"])
c = calculate_distance(points["P7"], points["P8"])

# 计算 (a + b) / c
ct_ratio = (a + b) / c

# 显示结果文本
ax.text(
    200,
    543,
    f"(a+b)/c = {ct_ratio:.2f}",
    color="red",
    fontsize=12,
    bbox=dict(facecolor="white", alpha=0.8),
)

# 显示图像
plt.show()
