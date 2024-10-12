import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# 定义创建圆形掩膜的函数
def create_circular_mask(shape, radius, is_high_pass=False):
    """生成以傅里叶中心为原点的圆形高通或低通遮罩"""
    rows, cols = shape
    center = (rows // 2, cols // 2)
    y, x = np.ogrid[:rows, :cols]
    dist_from_center = np.sqrt((x - center[1]) ** 2 + (y - center[0]) ** 2)

    # 生成低通或高通掩膜
    if is_high_pass:
        mask = dist_from_center > radius
    else:
        mask = dist_from_center <= radius

    # 处理半径为 0 的情况
    if radius == 0:
        if is_high_pass:
            mask[:, :] = 1  # 高通滤波器：保留所有频率（全白）
        else:
            mask[:, :] = 0  # 低通滤波器：滤除所有频率（全黑）
    return mask.astype(np.uint8)


def apply_filter(img, low_pass_radius, high_pass_radius):
    """应用高通和低通滤波"""
    # 傅里叶变换
    f_shift = np.fft.fftshift(np.fft.fft2(img))

    # 低通滤波
    lpf_mask = create_circular_mask(img.shape, low_pass_radius, is_high_pass=False)
    f_shift_lpf = f_shift * lpf_mask
    img_lpf = np.fft.ifft2(np.fft.ifftshift(f_shift_lpf)).real

    # 高通滤波
    hpf_mask = create_circular_mask(img.shape, high_pass_radius, is_high_pass=True)
    f_shift_hpf = f_shift * hpf_mask
    img_hpf = np.fft.ifft2(np.fft.ifftshift(f_shift_hpf)).real

    return img_lpf, img_hpf, lpf_mask, hpf_mask


def update(val):
    """更新图像的回调函数"""
    low_pass_radius = low_pass_slider.val
    high_pass_radius = high_pass_slider.val

    img_lpf, img_hpf, lpf_mask, hpf_mask = apply_filter(
        img, low_pass_radius, high_pass_radius
    )

    # 更新显示的低通和高通滤波图像
    lpf_img.set_data(img_lpf)
    hpf_img.set_data(img_hpf)

    # 更新遮罩显示
    lpf_mask_img.set_data(lpf_mask)
    hpf_mask_img.set_data(hpf_mask)

    fig.canvas.draw_idle()


# 读取图像并转换为灰度图
img = cv2.imread("advanced-6/1.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("图像无法读取")

# 创建 matplotlib 图像窗口
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# 显示原图
axs[0, 0].imshow(img, cmap="gray")
axs[0, 0].set_title("Original Image")
axs[0, 0].axis("off")

# 显示初始滤波图像
img_lpf, img_hpf, lpf_mask, hpf_mask = apply_filter(img, 20, 20)

# 在子图中显示滤波后的图像
lpf_img = axs[0, 1].imshow(img_lpf, cmap="gray")
axs[0, 1].set_title("Low-pass Filter")
axs[0, 1].axis("off")

hpf_img = axs[0, 2].imshow(img_hpf, cmap="gray")
axs[0, 2].set_title("High-pass Filter")
axs[0, 2].axis("off")

# 显示遮罩
lpf_mask_img = axs[1, 1].imshow(lpf_mask, cmap="gray")
axs[1, 1].set_title("Low-pass Mask")
axs[1, 1].axis("off")

hpf_mask_img = axs[1, 2].imshow(hpf_mask, cmap="gray")
axs[1, 2].set_title("High-pass Mask")
axs[1, 2].axis("off")

# 隐藏左下角的空白子图
axs[1, 0].axis("off")

# 创建滑动条
ax_lowpass = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_highpass = plt.axes([0.1, 0.05, 0.65, 0.03])

low_pass_slider = Slider(ax_lowpass, "Low-pass\nRadius", 0, 100, valinit=20)
high_pass_slider = Slider(ax_highpass, "High-pass\nRadius", 0, 100, valinit=20)

# 连接滑动条和更新函数
low_pass_slider.on_changed(update)
high_pass_slider.on_changed(update)

# 显示图像
plt.show()
