import base64
import background_setting as bg


def encoding(original_string):
    # 将字符串转为字节串，并使用UTF-8编码
    bytes_data = original_string.encode("utf-8")

    # 对字节串进行BASE64编码
    base64_encoded = base64.b64encode(bytes_data)

    # 将字节串转为字符串
    base64_encoded_string = base64_encoded.decode("utf-8")

    final_string = replace_characters(base64_encoded_string, bg.sign_array)
    return final_string


def replace_characters(string, sign_array):
    for sign_pair in sign_array:
        original_char, replacement = sign_pair
        string = string.replace(original_char, replacement)
    return string


def test():
    string_param = "2511410-[英訳]"
    result = encoding(string_param)
    print(result)
    print("length:", len(result))


# test()
