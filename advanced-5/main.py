import pydicom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def load_dicom_image(file_path):
    """加载DICOM图像并应用RescaleSlope和RescaleIntercept"""
    dicom_data = pydicom.dcmread(file_path)

    # 获取RescaleSlope和RescaleIntercept
    slope = dicom_data.get("RescaleSlope", 1)
    intercept = dicom_data.get("RescaleIntercept", 0)

    # 获取原始像素数据
    image_data = dicom_data.pixel_array

    # 应用灰度值转换
    image_data = image_data * slope + intercept
    return image_data


def apply_window_level(image_data, window_level, window_width):
    """应用窗宽窗位"""
    min_window = window_level - window_width // 2
    max_window = window_level + window_width // 2

    # 应用窗宽窗位（裁剪像素值）
    image_data = np.clip(image_data, min_window, max_window)

    # 归一化为0-255范围的灰度图
    image_data = (image_data - min_window) / (max_window - min_window) * 255
    image_data = np.uint8(image_data)

    return image_data


def display_image(image_data):
    """显示图像"""
    ax.imshow(image_data, cmap="gray")
    ax.axis("off")
    plt.draw()


def update(val):
    """更新窗宽窗位"""
    window_level = slider_level.val
    window_width = slider_width.val

    # 应用窗宽窗位
    windowed_image = apply_window_level(image_data, window_level, window_width)

    # 显示处理后的图像
    display_image(windowed_image)


# 载入CT图像
dicom_file_path = "advanced-5/1.dcm"
image_data = load_dicom_image(dicom_file_path)

# 设置初始窗宽窗位
initial_window_level = 40  # 初始窗位
initial_window_width = 400  # 初始窗宽

# 创建图形和轴
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.1, bottom=0.25)

# 显示初始图像
display_image(image_data)

# 添加窗宽和窗位的滑动条
ax_slider_level = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_width = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")

slider_level = Slider(
    ax_slider_level,
    "Window Level",
    -1000,
    1000,
    valinit=initial_window_level,
    valstep=1,
)
slider_width = Slider(
    ax_slider_width,
    "Window Width",
    2,
    2000,
    valinit=initial_window_width,
    valstep=1,
)

# 将滑动条与更新函数关联
slider_level.on_changed(update)
slider_width.on_changed(update)

plt.show()
