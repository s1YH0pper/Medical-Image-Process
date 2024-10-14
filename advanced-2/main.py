import cv2
import matplotlib.pyplot as plt

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

img1 = cv2.cvtColor(cv2.imread(img1_path), cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(cv2.imread(img2_path), cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1, descriptors_2)

matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(
    img1,
    keypoints_1,
    img2,
    keypoints_2,
    matches[:num_matches_to_display],
    img2,
    flags=2,
)

plt.imshow(img3)
plt.show()
