<div align="center">

# Medical-Image-Process

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<img src="https://img.shields.io/github/license/s1YH0pper/Medical-Image-Process.svg" alt="license">

一个基于 Python 的基本医学影像图像处理展示

</div>

## DEMO 目录

1. 基本图像处理 (basic-1)

   - 图像的平移、旋转、镜像和缩放

2. 噪声及滤波处理 (basic-2)

   经不同类型噪声污染后的退化图像, 以及两种常见的降噪滤波方法处理后的图像

   - 高斯噪声, 椒盐噪声和泊松噪声
   - 均值滤波和中值滤波对以上图像进行处理

3. 图像的形态学运算 (basic-3)

   四种常见形态学运算 (膨胀、腐蚀、开运算、闭运算), 以及不同图像算子的膨胀及腐蚀效果演示

4. 图像的平滑和锐化 (basic-4)

   不同平滑和锐化算法在医学图像处理中的作用

5. 医学图像 DCT 水印 (basic-5)

   基于 Arnold 置乱算法后的信息通过 DCT 嵌入图像

## 使用方法

1. 安装环境

   - 通过 pip 包管理导入环境

   ```bash
   pip install -r requirements_pip.txt
   ```

   - 通过 anaconda 或 miniconda

   ```bash
   conda create -n ENVNAME --file requirements_conda.txt
   ```

2. 运行对应目录下的`main.py`文件
