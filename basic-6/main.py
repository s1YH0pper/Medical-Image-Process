from skimage.segmentation import clear_border
from matplotlib import pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import (
    disk,
    binary_erosion,
    binary_closing,
)
from skimage.filters import roberts
from scipy import ndimage as ndi
import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt


def save_label_two_region(label_image):
    """保留两个最大的联通区域"""
    areas = [r.area for r in regionprops(label_image)]
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                    label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    return binary


def get_segmented_lungs(im, threshold=-300):
    """该函数用于从给定的2D切片中分割肺"""
    # 步骤1： 二值化
    binary = im < threshold

    # 步骤2： 清除边界上的斑点
    cleared = clear_border(binary)

    # 步骤3： 标记联通区域
    label_image = label(cleared)
    # 保留两个最大的联通区域，即左右肺部区域，其他区域全部置为0
    binary = save_label_two_region(label_image)

    # 腐蚀操作
    selem = disk(2)
    binary = binary_erosion(binary, selem)
    # 闭包操作
    selem = disk(10)
    binary = binary_closing(binary, selem)

    # 填充操作
    edges = roberts(binary)
    binary = ndi.binary_fill_holes(edges)

    # 返回最终的结果
    return binary


# 读取图片，一张CT切片的路径
path = "basic-6/1.dcm"
data = sitk.ReadImage(path)
spacing = data.GetSpacing()
scan = sitk.GetArrayFromImage(data)


# 显示原图
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(scan[0], cmap="gray")

# 获取当前CT切片的mask
mask = np.array([get_segmented_lungs(scan.copy().squeeze(0))])

# 将mask以外的值置为0，仅保留肺部结构
scan[~mask] = 0

# 显示分割结果
plt.subplot(1, 2, 2)
plt.title("Segmented Lung")
plt.imshow(scan[0], cmap="gray")
plt.show()
