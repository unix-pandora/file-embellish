import os
import shutil


def process_string(length):
    # 二进制字节串
    binary_data = b""

    # 如果二进制字节串的长度不足，用空格的二进制补齐
    while len(binary_data) < length:
        binary_data += b"\0"

    print("process_string binary_data: ", binary_data)
    return binary_data


def replace_byte_string(filepath, scope):
    # 创建临时文件路径
    temp_filepath = f"{filepath}.tmp"

    try:
        # 打开原文件以读写二进制模式
        with open(filepath, "r+b") as source_file:
            # 获取文件大小
            file_size = os.path.getsize(filepath)

            if file_size >= scope:  # 确保文件至少有 scope 个字节
                # 移动文件指针到第 scope 个字节的位置（从0开始计数）
                source_file.seek(scope)

                # 打开临时文件以写入二进制模式
                with open(temp_filepath, "wb") as temp_file:
                    # 将从第 (scope+1) 个字节开始的剩余内容写入临时文件
                    rest_of_content = source_file.read()
                    temp_file.write(rest_of_content)

        # 使用临时文件替换源文件
        os.replace(temp_filepath, filepath)

        print(f"Successfully removed the first '{scope}' bytes from '{filepath}'")
    except FileNotFoundError:
        print(f"File '{filepath}' does not exist.")
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        # 如果由于某种原因未能成功替换，并且临时文件存在，则删除临时文件
        if os.path.exists(temp_filepath) and os.path.isfile(temp_filepath):
            os.remove(temp_filepath)


def insert_bytes_at_start(file_path, new_bytes):
    try:
        # 创建临时文件
        temp_file_path = f"{file_path}.tmp"

        # 打开临时文件以写入二进制模式
        with open(temp_file_path, "wb") as temp_file:
            # 在临时文件中写入新的字节串
            temp_file.write(new_bytes)

            # 打开原始文件以读取二进制模式
            with open(file_path, "rb") as original_file:
                # 将原始文件的内容追加到临时文件
                shutil.copyfileobj(original_file, temp_file)

        # 替换原始文件为临时文件
        os.replace(temp_file_path, file_path)

        print(f"Success:'{file_path}' insert byte string at the beginning")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
    except Exception as e:
        print(f"An exception occur: {e}")
    finally:
        # 如果由于某种原因未能成功替换，确保删除临时文件
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
