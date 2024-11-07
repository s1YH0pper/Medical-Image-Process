from InquirerPy import prompt
import subprocess
import os


# 运行目录下 Python 文件的函数
def run_python_file(file_path):
    try:
        # 使用 subprocess 调用子目录中的 Python 文件
        subprocess.run(["python", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {file_path}: {e}")


# 子菜单：运行子目录下的 Python 文件
def submenu(menu_choice: str, submenu_dict: dict):
    while True:
        # 清空屏幕
        os.system("cls")
        # 动态生成choices列表，末尾添加"Back"选项
        choices = list(submenu_dict.keys()) + ["Back"]
        questions = [
            {
                "type": "list",
                "message": f"{menu_choice} - 选择要运行的:",
                "choices": choices,
                "name": "submenu_choice",
            }
        ]
        answer = prompt(questions)

        choice = answer["submenu_choice"]
        if choice == "Back":
            break  # 返回上一级菜单
        else:
            run_python_file(submenu_dict[choice])  # 根据选项运行对应的Python文件


# 主菜单
def main_menu(menu_dict: dict):
    while True:
        # 清空屏幕
        os.system("cls")
        # 动态生成choices列表，末尾添加"Exit"选项
        choices = list(menu_dict.keys()) + ["Exit"]
        questions = [
            {
                "type": "list",
                "message": "Main Menu - Select an option:",
                "choices": choices,
                "name": "menu_choice",
            }
        ]
        answer = prompt(questions)

        if answer["menu_choice"] != "Exit":
            submenu(
                answer["menu_choice"], menu_dict[answer["menu_choice"]]
            )  # 进入子菜单
        elif answer["menu_choice"] == "Exit":
            print("Exiting...")
            break  # 退出程序
