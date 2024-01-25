import os
import background_setting as bg


def check_create_directory(absolute_path):
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
        # print("Directory has created")
    # else:
    #     print("Directory already exist")


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


def recruit_root_path():
    separate = str(os.path.sep)

    final_log_dir = bg.project_root_directory + separate + bg.record_dir
    check_create_directory(final_log_dir)

    final_log_path = final_log_dir + separate
    final_log_path += bg.json_file_name
    # print("recruit_root_path: ", final_log_path)
    return final_log_path
