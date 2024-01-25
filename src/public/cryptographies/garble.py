from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

import background_setting as bg


# 需要补位，str不是16的倍数那就补足为16的倍数
def completion_key_str(key_str):
    key_str = str(key_str).strip()
    print("key_string length: ", len(key_str))

    if key_str is None:
        raise ValueError("completion_key_str: key_str can not be None")
    if len(key_str) < bg.keylength_upper_limit:
        key_str += "\0" * (bg.keylength_upper_limit - len(key_str))
    if len(key_str) > bg.keylength_upper_limit:
        key_str = key_str[: bg.keylength_upper_limit]

    key_byte = str.encode(key_str)  # 将字符串转换为字节串
    print("completion_key_byte: ", key_byte)
    return key_byte  # 将私钥字符串转换为字节对象,返回bytes


def encrypt(key, plain_text):
    print("encrypt key: ", key)

    # 检查 private_key 的长度是否为 16、24 或 32 字节，如果不是，则抛出 ValueError 异常
    if len(key) not in [16, 24, 32]:
        raise ValueError("The key length must be 16, 24, or 32 bytes")

    # 使用 AES（Advanced Encryption Standard）算法创建一个新的加密器对象，并设置工作模式为 CBC（Cipher Block Chaining）
    cipher = AES.new(key, AES.MODE_CBC)

    byte_content = plain_text.encode()  # 将内容转换为字节类型

    # 对个人密码进行填充，使其长度成为 AES 算法块大小的整数倍，然后使用加密器对象对其进行加密
    cipher_text = cipher.encrypt(pad(byte_content, AES.block_size))

    # 将加密后的密文和初始化向量连接起来，并使用 base64 进行编码，最后将结果转换为字符串并返回
    return base64.b64encode(cipher.iv + cipher_text).decode()


def decrypt(key, cipher_text):
    print("decrypt key: ", key)

    if len(key) not in [16, 24, 32]:
        raise ValueError("The key length must be 16, 24, or 32 bytes")

    # 使用 base64 进行解码，将密文字符串转换为字节对象
    encrypted_data = base64.b64decode(cipher_text)

    # 从加密数据中提取前 16 字节作为初始化向量（iv）
    iv = encrypted_data[:16]

    # 从加密数据中提取除去 iv 的剩余部分作为密文
    cipher_text = encrypted_data[16:]

    # 使用 AES 算法创建一个新的加密器对象，并设置工作模式为 CBC（Cipher Block Chaining）
    # iv 参数用于指定初始化向量，它是用于增加密码学安全性的随机数据块
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # 使用 AES 加密器对象对密文进行解密，并使用 unpad 函数去除填充的字节
    decrypted_content = cipher.decrypt(cipher_text)

    # 将解密后的数据（字节对象）转换为字符串并返回
    return unpad(decrypted_content, AES.block_size).decode()


def input_control(key, contnent, pattern):
    clean_keystr = str(key).strip()
    clean_contnentstr = str(contnent).strip()

    if clean_keystr is None or clean_contnentstr is None:
        return False

    if len(clean_keystr) > bg.keylength_upper_limit:
        return False

    clean_key_str = completion_key_str(clean_keystr)

    if pattern == 0:
        ciphertext = encrypt(clean_key_str, clean_contnentstr)
        return ciphertext
    elif pattern == 1:
        plain_text = decrypt(clean_key_str, clean_contnentstr)
        return plain_text
    else:
        return False
