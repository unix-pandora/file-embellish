import os


def write_to_file(content, textpath):
    content = str(content).strip()

    try:
        # 检查文件是否存在
        if not os.path.exists(textpath):
            # 如果文件不存在，创建文件及其上级目录
            os.makedirs(os.path.dirname(textpath), exist_ok=True)
            with open(textpath, "w") as file:
                file.write(content)
            print(f"Content has been successfully written to {textpath}")
        else:
            # 如果文件已经存在，直接写入内容
            with open(textpath, "w") as file:
                file.write(content)
            print(f"Content has been successfully written to {textpath}")
    except Exception as e:
        print(f"Error writing to {textpath}: {e}")
