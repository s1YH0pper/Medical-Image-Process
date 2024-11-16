import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg

# 读取图像
img = mpimg.imread("basic-7/1.jpg")

# 定义点坐标
points = {
    "P1": (75, 565),
    "P2": (51, 435),
    "P3": (95, 425),
}

# 绘制图像
fig, ax = plt.subplots()
ax.imshow(img)

# 绘制两条线段
ax.plot(
    [points["P1"][0], points["P2"][0]],
    [points["P1"][1], points["P2"][1]],
    linewidth=2,
    color="red",
    label="Line P1-P2",
)
ax.plot(
    [points["P1"][0], points["P3"][0]],
    [points["P1"][1], points["P3"][1]],
    linewidth=2,
    color="blue",
    label="Line P1-P3",
)

# 计算两条线段之间的夹角
vector1 = np.array(
    [points["P2"][0] - points["P1"][0], points["P2"][1] - points["P1"][1]]
)
vector2 = np.array(
    [points["P3"][0] - points["P1"][0], points["P3"][1] - points["P1"][1]]
)

# 计算夹角（弧度制）
cos_theta = np.dot(vector1, vector2) / (
    np.linalg.norm(vector1) * np.linalg.norm(vector2)
)
theta_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # 防止浮点误差导致的越界

# 将弧度转换为角度
theta_deg = np.degrees(theta_rad)

# 在图像上显示角度
ax.text(
    points["P1"][0] + 20,
    points["P1"][1] - 20,
    f"{theta_deg:.2f}°",
    color="red",
    fontsize=12,
    bbox=dict(facecolor="white", alpha=0.5),
)

# 添加图例
ax.legend(loc="upper right")

# 显示图像
plt.show()
