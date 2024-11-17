import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import medfilt2d
from scipy.fft import fft2, ifft2, fftshift, ifftshift


def add_salt_pepper_noise(image, prob):
    """添加椒盐噪声到图像中"""
    noisy = np.copy(image)
    num_salt = int(prob * image.size * 0.5)
    num_pepper = int(prob * image.size * 0.5)
    # 添加盐噪声
    salt_coords = [np.random.randint(0, dim - 1, num_salt) for dim in image.shape[:2]]
    noisy[salt_coords[0], salt_coords[1]] = 255
    # 添加椒噪声
    pepper_coords = [
        np.random.randint(0, dim - 1, num_pepper) for dim in image.shape[:2]
    ]
    noisy[pepper_coords[0], pepper_coords[1]] = 0
    return noisy


def motion_blur_psf(length, angle):
    """生成运动模糊点扩散函数（PSF）"""
    psf = np.zeros((length, length))
    center = length // 2
    x_end = center + int(length * np.cos(np.radians(angle)))
    y_end = center + int(length * np.sin(np.radians(angle)))
    cv2.line(psf, (center, center), (x_end, y_end), 1, thickness=1)
    return psf / psf.sum()


def wiener_filter(img, psf, K=0.0001):
    """对图像应用维纳滤波"""
    img_fft = fft2(img)
    psf_fft = fft2(psf, s=img.shape)
    psf_fft = np.conj(psf_fft) / (np.abs(psf_fft) ** 2 + K)
    img_deconv = np.abs(ifft2(img_fft * psf_fft))
    return np.uint8(np.clip(img_deconv, 0, 255))


# 读取原始图像
img = cv2.imread("advanced-1/1.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换为 RGB 格式

# 图像处理及可视化
plt.figure(figsize=(15, 8))

# 原图
plt.subplot(2, 4, 1)
plt.imshow(img_rgb)
plt.title("Original image")
plt.axis("off")

# 原图灰度化
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
plt.subplot(2, 4, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Gray image")
plt.axis("off")

# 添加椒盐噪声
noise_img = add_salt_pepper_noise(img_rgb, prob=0.05)
plt.subplot(2, 4, 3)
plt.imshow(noise_img)
plt.title("Salt-pepper noise image")
plt.axis("off")

# 转灰度图并中值滤波
noise_img_gray = cv2.cvtColor(noise_img, cv2.COLOR_RGB2GRAY)
med_filter_img = medfilt2d(noise_img_gray, kernel_size=3)
plt.subplot(2, 4, 4)
plt.imshow(med_filter_img, cmap="gray")
plt.title("Med-filter image")
plt.axis("off")

# 模拟运动模糊
LEN, THETA = 15, 15
PSF = motion_blur_psf(LEN, THETA)
blurred = cv2.filter2D(img_rgb, -1, PSF)
plt.subplot(2, 4, 5)
plt.imshow(blurred)
plt.title("blurred image")
plt.axis("off")

# 维纳滤波去模糊
wnrl = wiener_filter(blurred[:, :, 0], PSF)
plt.subplot(2, 4, 6)
plt.imshow(wnrl, cmap="gray")
plt.title("Wiener filter image")
plt.axis("off")

# 添加正弦噪声
m, n = img_gray.shape
sinoise_img = img_gray.astype(np.float64) + 50 * (
    np.sin(20 * np.arange(m)[:, None]) + np.sin(20 * np.arange(n))
)
plt.subplot(2, 4, 7)
plt.imshow(sinoise_img, cmap="gray")
plt.title("Sin-noise image")
plt.axis("off")

# 频域滤波去除正弦噪声
f = fft2(sinoise_img)
fshift = fftshift(f)
N1, N2 = fshift.shape
W, n, d0 = 50, 2, 83
n1, n2 = N1 // 2, N2 // 2

# 构建滤波器
H = 1 / (
    1
    + (
        (np.sqrt((np.arange(N1)[:, None] - n1) ** 2 + (np.arange(N2) - n2) ** 2) * W)
        / (
            d0**2
            - np.sqrt((np.arange(N1)[:, None] - n1) ** 2 + (np.arange(N2) - n2) ** 2)
            ** 2
        )
    )
    ** (2 * n)
)
filtered_freq = fshift * H
filtered_img = np.real(ifft2(ifftshift(filtered_freq)))
filtered_img = np.uint8(np.clip(filtered_img, 0, 255))

plt.subplot(2, 4, 8)
plt.imshow(filtered_img, cmap="gray")
plt.title("Filtered image")
plt.axis("off")

plt.tight_layout()
plt.show()
