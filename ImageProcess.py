import os
import sys
from PIL import Image
from ImageCut import Graphics


def getCurrentPath():
    dirName, fileName = os.path.split(sys.argv[0])
    return dirName + "/"


def list_img_file(directory):
    """列出目录下所有文件，并筛选出图片文件列表返回"""
    old_list = os.listdir(directory)
    # print old_list
    new_list = []
    for filename in old_list:
        name, fileformat = filename.split(".")
        if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
            new_list.append(filename)
    # print new_list
    return new_list


def make_directory(directory):
    """创建目录"""
    os.makedirs(directory)


def directory_exists(directory):
    """判断目录是否存在"""
    if os.path.exists(directory):
        return True
    else:
        return False


def image_process():
    """裁剪算法

    参数：None
    ------
    调用Graphics类中的裁剪算法，将src_dir目录下的文件进行裁剪（裁剪成正方形）
    """
    src_dir = getCurrentPath() + "photos/"
    dst_dir = getCurrentPath() + "cropped_photos/"
    if directory_exists(src_dir):
        if not directory_exists(src_dir):
            make_directory(src_dir)
        # business logic
        file_list = list_img_file(src_dir)
        # print file_list
        if file_list:
            # print_help()
            for infile in file_list:
                img = Image.open(src_dir + infile)
                #Graphics(infile=src_dir + infile, outfile=src_dir + infile).cut_by_ratio()  # 原地替换
                #Graphics(infile=src_dir + infile, outfile=dst_dir + infile).cut_by_ratio() #图片扩充为正方形
                Graphics(infile=src_dir + infile, outfile=dst_dir + infile).image_resize() #图像调整大小
                #Graphics(infile=src_dir + infile, outfile=dst_dir + infile).image_rotate() #图像旋转
        else:
            pass
    else:
        print("source directory not exist!")


if __name__ == "__main__":
    image_process()