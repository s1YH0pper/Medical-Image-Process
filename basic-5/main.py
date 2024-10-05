import subprocess


def main():
    print("选择要运行的代码:")
    print("1: 基于Arnold置乱的DCT图像加密")
    print("2: Arnold置乱图像还原")

    choice = input("请输入对应的数字（1-2）: ")

    if choice == "1":
        subprocess.run(["python", "basic-5/DCT image encryption.py"])
    elif choice == "2":
        subprocess.run(["python", "basic-5/arnold scramble recovery.py"])
    # elif choice == "3":
    #     subprocess.run(["python", "basic-5/DCT image encryption.py"])
    #     subprocess.run(["python", "basic-5/arnold scramble recovery.py"])
    else:
        print("无效选择，请重新运行程序。")


if __name__ == "__main__":
    main()
