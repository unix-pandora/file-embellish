import write_content as wc
import background_setting as bg
import garble


def write_cipher_in_file(password, content):
    # 加密：url_info_dict
    cipher_context = garble.input_control(password, content, bg.lock_pattern)
    if cipher_context == False:
        raise Exception("write_in_file Abnormal")

    # 写入
    wc.write_to_file(cipher_context, bg.json_file_path)
