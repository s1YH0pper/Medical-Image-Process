import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
I = cv2.imread("basic-3/1.jpg")

# Display original image
plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Dilation
SE_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
I_dilate = cv2.dilate(I, SE_dilate, iterations=1)
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(I_dilate, cv2.COLOR_BGR2RGB))
plt.title("Dilated Image")

# Erosion
SE_erode = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
I_erode = cv2.erode(I, SE_erode, iterations=1)
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(I_erode, cv2.COLOR_BGR2RGB))
plt.title("Eroded Image")

# Opening
I_open = cv2.morphologyEx(I, cv2.MORPH_OPEN, SE_dilate)
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(I_open, cv2.COLOR_BGR2RGB))
plt.title("Opened Image")

# Closing
I_close = cv2.morphologyEx(I, cv2.MORPH_CLOSE, SE_erode)
plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(I_close, cv2.COLOR_BGR2RGB))
plt.title("Closed Image")

plt.tight_layout()
plt.show()
