import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_image(image, title, position, cmap=None):
    plt.subplot(position)
    plt.imshow(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if cmap is None else image, cmap=cmap
    )
    plt.title(title)


# Read and convert image once
image = cv2.imread("./basic-1/1.jpg")

# Set up figure for displaying all transformations
plt.figure(figsize=(10, 10))

# Display original image
display_image(image, "Original Image (Comparison)", 221)

# Translation using warpAffine
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv2.warpAffine(
    image, translation_matrix, (image.shape[1], image.shape[0])
)
display_image(translated_image, "Translation", 222)

# Rotation
angle = -90
r_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
rotated_image = cv2.warpAffine(image, r_matrix, (image.shape[1], image.shape[0]))
display_image(rotated_image, "Rotation", 223)

# Mirroring (Horizontal flip)
mirror_image = cv2.flip(image, 1)
display_image(mirror_image, "Horizontal Symmetry", 224)

plt.tight_layout()
plt.show()

# Separate figure for scaling (as it's a larger zoom)
scale_factor = 5
scaled_image = cv2.resize(
    image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR
)
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))
plt.title("Zoom In")
plt.show()
