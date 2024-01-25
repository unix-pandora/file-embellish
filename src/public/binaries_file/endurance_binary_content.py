import background_setting as bg


def process_string(str_string, length):
    clean_str = str(str_string).strip()
    print("process_string clean_str.len", len(clean_str))

    # 检查输入条件
    if clean_str is None or len(clean_str) > bg.keylength_upper_limit:
        return False

    # 将字符串转换为二进制字节串
    binary_data = clean_str.encode("utf-8")

    # 如果二进制字节串的长度不足，用空格的二进制补齐
    while len(binary_data) < length:
        binary_data += b"\0"

    print("process_string binary_data: ", binary_data)
    return binary_data


def read_bytes_context(file_path, length):
    try:
        with open(file_path, "rb") as file:
            # 读取开头指定范围内的二进制内容
            content = file.read(length + 20)
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
    except Exception as e:
        print(f"An exception has occur: {e}")


def insert_bytes_at_start(file_path, new_bytes):
    try:
        with open(file_path, "rb") as file:
            # 读取文件的现有内容
            existing_content = file.read()

        # 在开头插入新的字节串
        modified_content = new_bytes + existing_content

        # 将修改后的内容写回文件
        with open(file_path, "wb") as file:
            file.write(modified_content)

        print(f"Success in file '{file_path}' insert byte string at the beginning")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
    except Exception as e:
        print(f"An exception occur: {e}")


def replace_byte_string(filepath, byte_string, scope):
    try:
        with open(filepath, "rb") as file:
            # 读取文件的前 scope 个字节
            content = file.read(scope)

        # 在 content 中查找 byte_string 的位置
        index = content.find(byte_string)

        if index != -1:
            # 如果找到了 byte_string，进行替换并重新写入文件
            replaced_content = (
                content[:index] + b"" + content[index + len(byte_string) :]
            )

            # 读取原文件的剩余内容
            with open(filepath, "rb") as file:
                remaining_content = file.read()[scope:]

            # 将替换后的内容和原文件的剩余内容合并，并写回文件
            with open(filepath, "wb") as file:
                file.write(replaced_content + remaining_content)

            print(
                f"File replaced successfully: '{filepath}', scope: {scope} , target: {byte_string}"
            )
        else:
            # 如果未找到 byte_string，则不做替换
            print(
                f"File: '{filepath}', scope: {scope}, not found: {byte_string}，The files remain as they are"
            )
    except FileNotFoundError:
        print(f"File '{filepath}' does exist")
    except Exception as e:
        print(f"An error occurred: {e}")


def test():
    file_path = "/home/user/Downloads/19035090_052_1d29.jpg"
    keyword = 9876543210
    new_bytes_data = process_string(keyword, bg.fringe_byte_length)
    print("len new_bytes_data", len(new_bytes_data))

    # insert_bytes_at_start(file_path, new_bytes_data)
    replace_byte_string(file_path, new_bytes_data, bg.fringe_byte_length + 10)

    result = read_bytes_context(file_path, bg.fringe_byte_length)
    print(f"binary content result: {result}")
    print("len result", len(result))


# test()
