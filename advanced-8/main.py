import cv2
import matplotlib.pyplot as plt
from skimage.color import label2rgb
from skimage.segmentation import watershed
from skimage.feature import canny
from skimage.morphology import reconstruction, disk, remove_small_objects, dilation
from skimage.measure import label


def morph_open_close_reconstruction(image):
    se = cv2.getStructuringElement(cv2.MORPH_DILATE, (10, 10))
    eroded = cv2.erode(image, se)
    reconstructed = reconstruction(eroded, image)
    dilated = cv2.dilate(reconstructed, se)
    closed_reconstructed = cv2.erode(dilated, se)
    return closed_reconstructed


def find_region_maximum(image, threshold):
    image = 255 - image
    fgm = image > threshold
    return 255 - fgm


def canny_edge_detect_and_fix_boundry(image):
    boundry_image = canny(image)
    boundry_image = remove_small_objects(boundry_image, min_size=1)
    boundry_image = dilation(boundry_image, disk(1))
    return boundry_image


# 读取图像并转换为灰度图像
image = cv2.imread("advanced-8/1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 6))
plt.subplot(241)
plt.imshow(gray, cmap="gray")
plt.title("Original Image")

# 形态学操作：开闭重建
closed_reconstructed = morph_open_close_reconstruction(gray)
plt.subplot(242)
plt.imshow(closed_reconstructed, cmap="gray")
plt.title("Opening-Closing Reconstruction")

fgm = find_region_maximum(closed_reconstructed, 80)
plt.subplot(243)
plt.imshow(fgm, cmap="gray")
plt.title("Foreground markers")

# 标记连通区域（分水岭盆地）
labeled_fgm = label(fgm, connectivity=None)
watershed_lung_right = labeled_fgm == 4
watershed_lung_left = labeled_fgm == 5
watershed_lung = watershed_lung_right + watershed_lung_left
plt.subplot(244)
plt.imshow(watershed_lung, cmap="gray")
plt.title("Watershed Basins")

# 使用Canny边缘检测修正边界
boundary_mask = canny_edge_detect_and_fix_boundry(watershed_lung)

# 显示修正后的边界
plt.subplot(245)
plt.imshow(boundary_mask, cmap="gray")
plt.title("Boundary correction")

# 显示分割的边界图像
plt.subplot(246)
plt.imshow(image)
plt.imshow(boundary_mask, alpha=0.3)
plt.title("Segmented Image")

# 进行分水岭变换
watershed_mask = watershed(boundary_mask)

# 颜色标记分水岭区域
rgb_mask = label2rgb(watershed_mask, bg_label=0)
plt.subplot(247)
plt.imshow(image)
plt.imshow(rgb_mask, alpha=0.3)
plt.title("Segmented Image(Watershed)")

plt.tight_layout()
plt.show()
