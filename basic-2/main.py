import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread("./basic-2/1.jpg")
plt.figure(figsize=(6, 8))

# Display original image
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

# Convert to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Add Gaussian noise
gauss_img = cv2.GaussianBlur(gray_img, (0, 0), 1.0, 0.1)
plt.subplot(2, 2, 2)
plt.imshow(gauss_img, cmap="gray")
plt.title("Gaussian Noise Image")

# Add salt and pepper noise
sp_img = np.copy(gray_img)
num_salt = np.ceil(0.05 * gray_img.size).astype(int)
coords = [np.random.randint(0, i - 1, num_salt) for i in gray_img.shape]
sp_img[coords[0], coords[1]] = 255  # Add salt (white pixels)

num_pepper = np.ceil(0.05 * gray_img.size).astype(int)
coords = [np.random.randint(0, i - 1, num_pepper) for i in gray_img.shape]
sp_img[coords[0], coords[1]] = 0  # Add pepper (black pixels)

plt.subplot(2, 2, 3)
plt.imshow(sp_img, cmap="gray")
plt.title("Salt and Pepper Noise Image")


# Add Poisson noise
lambda_ = 10  # Adjust lambda value to control Poisson noise intensity
ps_img = np.random.poisson(gray_img / 255.0 * lambda_) * 255.0 / lambda_
plt.subplot(2, 2, 4)
plt.imshow(ps_img, cmap="gray")
plt.title("Poisson Noise Image")

# Mean filtering
gauss_img_average_filter = cv2.blur(gauss_img, (3, 3))
sp_img_average_filter = cv2.blur(sp_img, (3, 3))
ps_img_average_filter = cv2.blur(ps_img, (3, 3))

plt.figure(figsize=(6, 8))
plt.subplot(2, 2, 2)
plt.imshow(gauss_img_average_filter, cmap="gray")
plt.title("3x3 Mean Filter on Gaussian Noise")
plt.subplot(2, 2, 3)
plt.imshow(sp_img_average_filter, cmap="gray")
plt.title("3x3 Mean Filter on\nSalt and Pepper Noise")
plt.subplot(2, 2, 4)
plt.imshow(ps_img_average_filter, cmap="gray")
plt.title("3x3 Mean Filter on Poisson Noise")

# Median filtering
gauss_img_medfilt = cv2.medianBlur(gauss_img, 3)
sp_img_medfilt = cv2.medianBlur(sp_img, 3)
ps_img_medfilt = cv2.medianBlur(ps_img.astype(np.uint8), 3)

plt.figure(figsize=(6, 8))
plt.subplot(2, 2, 2)
plt.imshow(gauss_img_medfilt, cmap="gray")
plt.title("3x3 Median Filter on Gaussian Noise")
plt.subplot(2, 2, 3)
plt.imshow(sp_img_medfilt, cmap="gray")
plt.title("3x3 Median Filter on\nSalt and Pepper Noise")
plt.subplot(2, 2, 4)
plt.imshow(ps_img_medfilt, cmap="gray")
plt.title("3x3 Median Filter on Poisson Noise")

plt.show()
