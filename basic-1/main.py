import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("./basic-1/1.jpg")

# Display original image
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image (Comparison)")

# Translation
se = np.array([[0, 0, 0], [0, 0, 0], [-100, 50, 1]], dtype=np.uint8)
bw_img = cv2.dilate(image, se, iterations=1)
plt.figure(figsize=(6, 6))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(bw_img, cv2.COLOR_BGR2RGB))
plt.title("Translation")

# Rotation
n = -90
rows, cols, _ = image.shape
r_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), n, 1)
r_img = cv2.warpAffine(image, r_matrix, (cols, rows))
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(r_img, cv2.COLOR_BGR2RGB))
plt.title("Rotation")

# Mirroring
mirror_img = cv2.flip(image, 1)
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(mirror_img, cv2.COLOR_BGR2RGB))
plt.title("Horizontal Symmetry")

# Scaling
scale_factor = 5
image3 = cv2.resize(
    image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR
)
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("Zoom In")

plt.show()
