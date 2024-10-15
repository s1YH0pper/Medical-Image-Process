import subprocess


def main():
    print("选择要运行的代码:")
    print("1: 基于彩色变换法的伪彩处理")
    print("2: 基于密度分层法的伪彩处理")

    choice = input("请输入对应的数字（1-2）: ")

    if choice == "1":
        subprocess.run(["python", "basic-8/Color Transformation.py"])
    elif choice == "2":
        subprocess.run(["python", "basic-8/Intensity Slicing.py"])
    else:
        print("无效选择，请重新运行程序。")


if __name__ == "__main__":
    main()
