import base64
import background_setting as bg


def decoding(base64_encoded_string):
    initialize_string = reverse_replace_chars(base64_encoded_string, bg.sign_array)

    # 对BASE64编码的字符串进行解码
    base64_decoded = base64.b64decode(initialize_string)

    # 将解码后的字节串转为字符串，并使用UTF-8解码
    decoded_string = base64_decoded.decode("utf-8")
    return decoded_string


def reverse_replace_chars(string, sign_array):
    for sign_pair in sign_array:
        original_char, replacement = sign_pair
        string = string.replace(replacement, original_char)
    return string


def test():
    param = "MjUxMTQxMC1b44Oe44K444Kr44Or4piG44G_p_44Gq44GqICjjgb7jgarjgaopXSDmlofjga7nsbPjgYzlm6DmlYXjgarlubbimYLjgafjg57jg4PjgrXjg7zjgrjjgZXjgozjgosgW_p_iLseios10_e_"
    result = decoding(param)
    print(result)


# test()
