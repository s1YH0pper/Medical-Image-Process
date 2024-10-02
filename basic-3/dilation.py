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

# Diamond-shaped dilation
SE_diamond_dilate = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
I_diamond_dilate = cv2.dilate(image, SE_diamond_dilate)
plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(I_diamond_dilate, cmap="gray")
plt.title("Diamond Dilation Image")
plt.axis("off")

# Disk-shaped dilation
SE_disk_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
I_disk_dilate = cv2.dilate(image, SE_disk_dilate)
plt.subplot(2, 3, 2)
plt.imshow(I_disk_dilate, cmap="gray")
plt.title("Disk Dilation Image")
plt.axis("off")

# Line dilation
SE_line_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 15))
I_line_dilate = cv2.dilate(image, SE_line_dilate)
plt.subplot(2, 3, 3)
plt.imshow(I_line_dilate, cmap="gray")
plt.title("Line Dilation Image")
plt.axis("off")

# Square dilation
SE_square_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
I_square_dilate = cv2.dilate(image, SE_square_dilate)
plt.subplot(2, 3, 4)
plt.imshow(I_square_dilate, cmap="gray")
plt.title("Square Dilation Image")
plt.axis("off")

# Octagon dilation
# Create a custom octagon kernel
SE_octagon_dilate = np.array(
    [
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
    ],
    dtype=np.uint8,
)
I_octagon_dilate = cv2.dilate(image, SE_octagon_dilate)
plt.subplot(2, 3, 5)
plt.imshow(I_octagon_dilate, cmap="gray")
plt.title("Octagon Dilation Image")
plt.axis("off")

# Ball-shaped dilation
SE_ball_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
I_ball_dilate = cv2.dilate(image, SE_ball_dilate)
plt.subplot(2, 3, 6)
plt.imshow(I_ball_dilate, cmap="gray")
plt.title("Ball Dilation Image")
plt.axis("off")

plt.tight_layout()
plt.show()
