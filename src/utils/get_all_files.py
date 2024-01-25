import os


# 根据路径递归遍历获取该路径下的全部文件（包含子目录下的文件）的绝对路径
def get_all_files(directory):
    all_files = []

    # 递归遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)

    return all_files
