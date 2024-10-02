import subprocess


def main():
    print("选择要运行的代码:")
    print("1: 基本形态学运算演示")
    print("2: 几种不同形态shape的膨胀")
    print("3: 几种不同形态shape的腐蚀")

    choice = input("请输入对应的数字（1-3）: ")

    if choice == "1":
        subprocess.run(["python", "basic-3\\basic_morph.py"])
    elif choice == "2":
        subprocess.run(["python", "basic-3\\erosion.py"])
    elif choice == "3":
        subprocess.run(["python", "basic-3\\dilation.py"])
    elif choice == "4":
        subprocess.run(["python", "basic-3\\basic_morph.py"])
        subprocess.run(["python", "basic-3\\erosion.py"])
        subprocess.run(["python", "basic-3\\dilation.py"])
    else:
        print("无效选择，请重新运行程序。")


if __name__ == "__main__":
    main()
