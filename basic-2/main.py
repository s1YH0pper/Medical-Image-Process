import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_image(image, cmap, title, subplot_position):
    plt.subplot(subplot_position)
    plt.imshow(image, cmap=cmap)
    plt.title(title)


# Read image
image = cv2.imread("./basic-2/1.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Display original image
plt.figure(figsize=(6, 8))
display_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), None, "Original Image", 221)

# Add Gaussian noise
gauss_noise = np.random.normal(0, 25, gray_img.shape)
gauss_img = np.clip(gray_img + gauss_noise, 0, 255).astype(np.uint8)
display_image(gauss_img, "gray", "Gaussian Noise", 222)

# Add salt and pepper noise
sp_img = np.copy(gray_img)
num_salt = np.ceil(0.05 * gray_img.size).astype(int)
coords_salt = [np.random.randint(0, i - 1, num_salt) for i in gray_img.shape]
sp_img[coords_salt[0], coords_salt[1]] = 255

num_pepper = np.ceil(0.05 * gray_img.size).astype(int)
coords_pepper = [np.random.randint(0, i - 1, num_pepper) for i in gray_img.shape]
sp_img[coords_pepper[0], coords_pepper[1]] = 0
display_image(sp_img, "gray", "Salt and Pepper Noise", 223)

# Add Poisson noise
poisson_noise = np.random.poisson(gray_img / 255.0 * 10) * (255.0 / 10)
ps_img = np.clip(poisson_noise, 0, 255).astype(np.uint8)
display_image(ps_img, "gray", "Poisson Noise", 224)

plt.tight_layout()
plt.show()

# Mean filtering
gauss_img_avg = cv2.blur(gauss_img, (3, 3))
sp_img_avg = cv2.blur(sp_img, (3, 3))
ps_img_avg = cv2.blur(ps_img, (3, 3))

plt.figure(figsize=(6, 8))
display_image(gauss_img_avg, "gray", "Mean Filter (Gaussian)", 222)
display_image(sp_img_avg, "gray", "Mean Filter (Salt & Pepper)", 223)
display_image(ps_img_avg, "gray", "Mean Filter (Poisson)", 224)

# Median filtering
gauss_img_med = cv2.medianBlur(gauss_img, 3)
sp_img_med = cv2.medianBlur(sp_img, 3)
ps_img_med = cv2.medianBlur(ps_img, 3)

plt.figure(figsize=(6, 8))
display_image(gauss_img_med, "gray", "Median Filter (Gaussian)", 222)
display_image(sp_img_med, "gray", "Median Filter (Salt & Pepper)", 223)
display_image(ps_img_med, "gray", "Median Filter (Poisson)", 224)

plt.tight_layout()
plt.show()
