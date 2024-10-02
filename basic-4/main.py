import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image and convert to grayscale
i = cv2.imread("basic-4/1.jpg", cv2.IMREAD_GRAYSCALE)

# Create a subplot layout
plt.figure(figsize=(12, 6))

# Prewitt operator
prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
prewitt_i_x = cv2.filter2D(
    i.astype(np.float32), -1, prewitt_kernel_x, borderType=cv2.BORDER_REFLECT
)
prewitt_i_y = cv2.filter2D(
    i.astype(np.float32), -1, prewitt_kernel_y, borderType=cv2.BORDER_REFLECT
)
prewitt_i = np.uint8(
    np.clip(np.sqrt(np.square(prewitt_i_x) + np.square(prewitt_i_y)), 0, 255)
)
plt.subplot(2, 4, 1)
plt.imshow(prewitt_i, cmap="gray")
plt.title("Prewitt Operator")

# Sobel operator
sobel_i_x = cv2.Sobel(
    i.astype(np.float32), cv2.CV_64F, 1, 0, ksize=3, borderType=cv2.BORDER_REFLECT
)
sobel_i_y = cv2.Sobel(
    i.astype(np.float32), cv2.CV_64F, 0, 1, ksize=3, borderType=cv2.BORDER_REFLECT
)
sobel_i = np.uint8(
    np.clip(np.sqrt(np.square(sobel_i_x) + np.square(sobel_i_y)), 0, 255)
)
plt.subplot(2, 4, 2)
plt.imshow(sobel_i, cmap="gray")
plt.title("Sobel Operator")


# LoG operator
def log_filter(size=5, sigma=1.0):
    """Generate LoG kernel"""
    kernel = np.zeros((size, size), dtype=np.float32)
    center = size // 2
    for x in range(size):
        for y in range(size):
            x_diff = x - center
            y_diff = y - center
            kernel[x, y] = (
                -(1 / (np.pi * sigma**4))
                * (1 - (x_diff**2 + y_diff**2) / (2 * sigma**2))
                * np.exp(-(x_diff**2 + y_diff**2) / (2 * sigma**2))
            )
    return kernel


log_kernel = log_filter(size=5, sigma=1.0)
log_i = cv2.filter2D(
    i.astype(np.float32), -1, log_kernel, borderType=cv2.BORDER_REFLECT
)
log_i = np.clip(log_i, 0, 255).astype(np.uint8)
plt.subplot(2, 4, 3)
plt.imshow(log_i, cmap="gray")
plt.title("LoG Operator")

# Laplacian operator
laplacian_i = cv2.Laplacian(i, cv2.CV_64F)
laplacian_i = np.uint8(np.clip(laplacian_i, 0, 255))
plt.subplot(2, 4, 4)
plt.imshow(laplacian_i, cmap="gray")
plt.title("Laplacian Operator")

# Original image overlay
plt.subplot(2, 4, 5)
plt.imshow(np.clip(i + prewitt_i, 0, 255), cmap="gray")
plt.title("Prewitt Overlay")

plt.subplot(2, 4, 6)
plt.imshow(np.clip(i + sobel_i, 0, 255), cmap="gray")
plt.title("Sobel Overlay")

plt.subplot(2, 4, 7)
plt.imshow(np.clip(i + log_i, 0, 255), cmap="gray")
plt.title("LoG Overlay")

plt.subplot(2, 4, 8)
plt.imshow(np.clip(i + laplacian_i, 0, 255), cmap="gray")
plt.title("Laplacian Overlay")

plt.tight_layout()
plt.show()
