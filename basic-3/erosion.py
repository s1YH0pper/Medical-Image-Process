import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("basic-3/2.png", cv2.IMREAD_GRAYSCALE)

# Display original image
plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Diamond-shaped erosion
se_diamond_erode = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
I_diamond_erode = cv2.erode(image, se_diamond_erode)
plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(I_diamond_erode, cmap="gray")
plt.title("Diamond Erosion Image")
plt.axis("off")

# Disk-shaped erosion
se_disk_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
I_disk_erode = cv2.erode(image, se_disk_erode)
plt.subplot(2, 3, 2)
plt.imshow(I_disk_erode, cmap="gray")
plt.title("Disk Erosion Image")
plt.axis("off")

# Line erosion
se_line_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
I_line_erode = cv2.erode(image, se_line_erode)
plt.subplot(2, 3, 3)
plt.imshow(I_line_erode, cmap="gray")
plt.title("Line Erosion Image")
plt.axis("off")

# Square erosion
se_square_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
I_square_erode = cv2.erode(image, se_square_erode)
plt.subplot(2, 3, 4)
plt.imshow(I_square_erode, cmap="gray")
plt.title("Square Erosion Image")
plt.axis("off")

# Octagon erosion
# Create a custom octagon kernel
se_octagon_erode = np.array(
    [
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
    ],
    dtype=np.uint8,
)
I_octagon_erode = cv2.erode(image, se_octagon_erode)
plt.subplot(2, 3, 5)
plt.imshow(I_octagon_erode, cmap="gray")
plt.title("Octagon Erosion Image")
plt.axis("off")

# Ball-shaped erosion
se_ball_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
I_ball_erode = cv2.erode(image, se_ball_erode)
plt.subplot(2, 3, 6)
plt.imshow(I_ball_erode, cmap="gray")
plt.title("Ball Erosion Image")
plt.axis("off")

plt.tight_layout()
plt.show()
