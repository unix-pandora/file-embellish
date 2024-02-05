import os


def check_create_directory(absolute_path):
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)


def find_file(filename, start_directory="."):
    current_directory = os.path.abspath(start_directory)

    # 在当前目录中查找文件
    file_path = os.path.join(current_directory, filename)
    if os.path.isfile(file_path):
        return file_path

    # 如果未找到文件，向上一级目录递归查找
    parent_directory = os.path.dirname(current_directory)
    if current_directory == parent_directory:
        # 已经到达顶层目录，文件未找到
        return "."

    # 递归调用，向上一级目录查找
    return find_file(filename, parent_directory)
