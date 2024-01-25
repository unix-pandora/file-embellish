from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

import background_setting as bg
import front_reception as fr


def keyword_to_bytes(keyword: str) -> bytes:
    keyword = str(keyword).strip()
    length_limit = int(bg.keylength_upper_limit / 2)

    if keyword is None:
        raise ValueError("Parameter: keyword can not be None")
    if len(keyword) < length_limit:
        keyword += "\0" * (length_limit - len(keyword))
    if len(keyword) > length_limit:
        keyword = keyword[:length_limit]

    key_bytes = keyword.encode()
    print("length of key_bytes: ", len(key_bytes))
    return key_bytes


def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode()


def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decoded_ciphertext = base64.b64decode(ciphertext.encode())
    padded_plaintext = cipher.decrypt(decoded_ciphertext)
    return unpad(padded_plaintext, DES.block_size).decode()


def test():
    key_bytes = keyword_to_bytes(fr.security_pass)
    plaintext = "Hello, world!"

    encrypted_text = des_encrypt(plaintext, key_bytes)
    print("encrypted_text：", encrypted_text)

    decrypted_text = des_decrypt(encrypted_text, key_bytes)
    print("decrypted_text：", decrypted_text)


# test()
