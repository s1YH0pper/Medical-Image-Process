import cv2
import cv2.typing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# 读取图像并转换为灰度图像
def load_and_convert_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray_image


# 区域生长算法
def region_growing(image, seed_point, threshold=25):
    m, n = image.shape
    seed_value = image[seed_point[1], seed_point[0]]
    mask = np.zeros((m, n), dtype=np.uint8)
    mask[seed_point[1], seed_point[0]] = 1
    region_sum = seed_value
    region_count = 1
    suit = 1

    while region_count > 0:
        s = 0
        region_count = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if mask[i, j] == 1:
                    for u in range(-3, 4):
                        for v in range(-3, 4):
                            if (
                                mask[i + u, j + v] == 0
                                and abs(image[i + u, j + v] - seed_value) <= threshold
                                and 1
                                / (1 + 1 / 15 * abs(image[i + u, j + v] - seed_value))
                                > 0.6
                            ):
                                mask[i + u, j + v] = 1
                                region_count += 1
                                s += image[i + u, j + v]

        suit += region_count
        region_sum += s
        seed_value = region_sum / suit

    return mask


# 膨胀处理
def mask_dialation(region_mask):
    dilated_mask = cv2.dilate(
        region_mask.astype(np.uint8), np.ones((3, 3), np.uint8), iterations=1
    )
    return dilated_mask


# 标记区域并进行颜色标注
def mark_region(image, mask):
    R, G, B = cv2.split(image)
    R[mask == 1] = 255
    G[mask == 1] = 0
    B[mask == 1] = 0
    marked_image = cv2.merge([R, G, B])
    return marked_image


# 计算区域属性：质心和边界框
def calculate_region_properties(mask):
    contours, _ = cv2.findContours(
        mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if contours:
        contour = max(contours, key=cv2.contourArea)  # 找到最大轮廓
        M = cv2.moments(contour)
        if M["m00"] != 0:
            centroid_x = int(M["m10"] / M["m00"])
            centroid_y = int(M["m01"] / M["m00"])
        else:
            centroid_x, centroid_y = 0, 0
        x, y, w, h = cv2.boundingRect(contour)
        return (centroid_x, centroid_y), (x, y, w, h)
    return (0, 0), (0, 0, 0, 0)


# 显示图像和标注
def display_results(original, mask, dilated_mask, marked_image, centroid, bounding_box):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    axes[0, 0].imshow(original, cmap="gray")
    axes[0, 0].set_title("Original Image")

    axes[0, 1].imshow(mask, cmap="gray")
    axes[0, 1].set_title("Region Grown Mask")

    axes[1, 0].imshow(dilated_mask, cmap="gray")
    axes[1, 0].set_title("Dilated Mask")

    axes[1, 1].imshow(marked_image)
    axes[1, 1].set_title("Marked Image")

    # 在图像上标记质心和边界框
    axes[1, 1].plot(centroid[0], centroid[1], "r+", markersize=12)
    rect = Rectangle(
        (bounding_box[0], bounding_box[1]),
        bounding_box[2],
        bounding_box[3],
        edgecolor="r",
        facecolor="none",
        linewidth=1,
    )
    axes[1, 1].add_patch(rect)

    plt.show()


def main():
    print("选择要处理的图像:")
    print("1: 肝脏海绵状血管瘤 CT 图像")
    print("2: 颅脑肿瘤 MRI 图像")

    choice = input("请输入对应的数字(1-2): ")

    if choice == "1":
        img_path = "advanced-4/1.jpg"
        seed_point = (189, 109)
    elif choice == "2":
        img_path = "advanced-4/2.jpg"
        seed_point = (125, 227)
    else:
        print("无效选择，请重新运行程序。")
        exit()

    original_image, gray_image = load_and_convert_image(img_path)

    seed_point_choice = input("是否手动选择种子点, 第一次建议选择否(y/[n]):").lower()
    if seed_point_choice == "y":
        # 手动选择种子点
        plt.imshow(gray_image, cmap="gray")
        select_point = plt.ginput(1)
        seed_point = (int(select_point[0][0]), int(select_point[0][1]))
        plt.close()

    # 区域生长算法
    region_mask = region_growing(gray_image, seed_point)

    # 膨胀处理
    dilated_mask = mask_dialation(region_mask)

    # 标记区域
    marked_image = mark_region(original_image, dilated_mask)

    # 计算区域属性
    centroid, bounding_box = calculate_region_properties(region_mask)

    # 显示结果
    display_results(
        gray_image, region_mask, dilated_mask, marked_image, centroid, bounding_box
    )


if __name__ == "__main__":
    main()
