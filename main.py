import cli_selector


basic_menu_options = {
    "1. 基本图像处理": "basic-1/main.py",
    "2. 噪声及滤波处理": "basic-2/main.py",
    "3. 图像的形态学运算": "basic-3/main.py",
    "4. 图像的平滑和锐化": "basic-4/main.py",
    "5. 医学图像 DCT 水印": "basic-5/main.py",
    "6. CT 图像肺实质分割": "basic-6/main.py",
    "7. 医学图像数值的测量": "basic-7/main.py",
    "8. 医学图像伪彩处理": "basic-8/main.py",
}

advanced_menu_options = {
    "1. 退化医学图像的复原": "advanced-1/main.py",
    "2. 基于 SIFT 算法的医学图像配准": "advanced-2/main.py",
    "3. 不同模态医学图像的融合": "advanced-3/main.py",
    "4. 医学图像病变部位的标记": "advanced-4/main.py",
    "5. CT 图像的窗宽和窗位": "advanced-5/main.py",
    "6. MRI 图像的频率域滤波": "advanced-6/main.py",
    "7. MRI 图像的增强处理": "advanced-7/main.py",
    "8. 基于分水岭算法的病变区域分割": "advanced-8/main.py",
}
menu_dict = {"基础(basic)": basic_menu_options, "高级(advanced)": advanced_menu_options}

if __name__ == "__main__":
    cli_selector.main_menu(menu_dict)
