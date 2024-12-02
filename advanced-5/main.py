import pydicom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


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


def set_predefined_window(val):
    """设置常用窗宽窗位"""
    # 根据按钮标签设置对应的窗宽窗位
    predefined_values = {
        "Soft Tissue": (40, 400),
        "Lung": (-600, 1500),
        "Bone": (500, 1500),
        "Brain": (40, 80),
        "Abdomen": (50, 350),
    }

    window_center, window_width = predefined_values[val]
    slider_level.set_val(window_center)
    slider_width.set_val(window_width)

    # 更新图像显示
    windowed_image = apply_window_level(image_data, window_center, window_width)
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

# 创建常用窗宽窗位按钮
ax_soft_tissue = plt.axes([0.0, 0.25, 0.2, 0.05])
ax_lung = plt.axes([0.2, 0.25, 0.2, 0.05])
ax_bone = plt.axes([0.4, 0.25, 0.2, 0.05])
ax_brain = plt.axes([0.6, 0.25, 0.2, 0.05])
ax_abdomen = plt.axes([0.8, 0.25, 0.2, 0.05])

button_soft_tissue = Button(ax_soft_tissue, "Soft Tissue")
button_lung = Button(ax_lung, "Lung")
button_bone = Button(ax_bone, "Bone")
button_brain = Button(ax_brain, "Brain")
button_abdomen = Button(ax_abdomen, "Abdomen")

# 为按钮绑定事件
button_soft_tissue.on_clicked(lambda event: set_predefined_window("Soft Tissue"))
button_lung.on_clicked(lambda event: set_predefined_window("Lung"))
button_bone.on_clicked(lambda event: set_predefined_window("Bone"))
button_brain.on_clicked(lambda event: set_predefined_window("Brain"))
button_abdomen.on_clicked(lambda event: set_predefined_window("Abdomen"))

plt.show()
