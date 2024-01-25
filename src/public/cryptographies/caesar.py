def caesar_cipher_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            # 对字母进行移位，保持大小写
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # 非字母字符不进行移位
            result += char
    return result


def caesar_cipher_decrypt(ciphertext, shift):
    # 解密即加密的逆操作，使用负向移位
    return caesar_cipher_encrypt(ciphertext, -shift)
