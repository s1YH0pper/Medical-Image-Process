import subprocess


def main():
    print("选择要运行的代码:")
    print("1: 肋膈角的测量")
    print("2: 心胸比(CT-ratio)的测量")

    choice = input("请输入对应的数字（1-2）: ")

    if choice == "1":
        subprocess.run(["python", "basic-7/costophrenic angle.py"])
    elif choice == "2":
        subprocess.run(["python", "basic-7\ct_ratio.py"])
    else:
        print("无效选择，请重新运行程序。")


if __name__ == "__main__":
    main()
