import cv2
import matplotlib.pyplot as plt


# 定义函数用于读取并转换图像为灰度图
def load_and_convert_to_gray(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Unable to load image at path: {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


print("选择要配准的图像:")
print("1: 大小不同的图像")
print("2: 明暗不同的图像")
print("3: 角度不同的图像")
print("4: 部分区域交集的图像")

choice = input("请输入对应的数字(1-4): ")
num_matches_to_display = input(
    "请输入显示匹配点的数量(越多准确度越低, 推荐50, 直接回车默认50): "
)
num_matches_to_display = int(num_matches_to_display) if num_matches_to_display else 50

if choice == "1":
    img1_path, img2_path = "advanced-2/1.jpg", "advanced-2/2.jpg"
elif choice == "2":
    img1_path, img2_path = "advanced-2/1.jpg", "advanced-2/3.jpg"
elif choice == "3":
    img1_path, img2_path = "advanced-2/1.jpg", "advanced-2/4.jpg"
elif choice == "4":
    img1_path, img2_path = "advanced-2/a.png", "advanced-2/b.png"
else:
    print("无效选择，请重新运行程序。")
    exit()

# 尝试加载图像
try:
    img1 = load_and_convert_to_gray(img1_path)
    img2 = load_and_convert_to_gray(img2_path)
except FileNotFoundError as e:
    print(e)
    exit()

sift = cv2.SIFT_create()

# 检测关键点和描述符
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

if descriptors_1 is None or descriptors_2 is None:
    raise ValueError(
        "No descriptors found in one or both images, unable to proceed with matching."
    )

# 使用 Brute-Force Matcher 进行匹配
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(descriptors_1, descriptors_2)

# 根据距离排序匹配点，距离越小表示匹配越好
matches = sorted(matches, key=lambda x: x.distance)

# 限制显示的匹配点数量
img3 = cv2.drawMatches(
    img1,
    keypoints_1,
    img2,
    keypoints_2,
    matches[:num_matches_to_display],
    None,
    flags=2,
)

plt.figure(figsize=(10, 5))
plt.imshow(img3, cmap="gray")
plt.title(f"Top {num_matches_to_display} Feature Matches")
plt.axis("off")
plt.show()
