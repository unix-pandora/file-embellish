import falsify as falsify
import front_reception as fr
import base_encode as bec
import decode_base as dba

# useless and waste file


def encrypt_encoding(name_str):
    pwd_bytes = falsify.keyword_to_bytes(fr.security_pass)
    cipher_string = falsify.des_encrypt(name_str, pwd_bytes)

    encode_result = bec.encoding(cipher_string)
    return encode_result


def decode_decrypt(name_str):
    primitive_text = dba.decoding(name_str)

    pwd_bytes = falsify.keyword_to_bytes(fr.security_pass)
    plain_string = falsify.des_decrypt(primitive_text, pwd_bytes)
    return plain_string


def test():
    filename = "MjUxMTQxMC1b44Oe44K444Kr44Or4piG44G_p_44Gq44GqICjjgb7jgarjgaopXSDmlofjga7nsbPjgYzlm6DmlYXjgarlubbimYLjgafjg57jg4PjgrXjg7zjgrjjgZXjgozjgosgW_p_iLseios10_e_"

    result1 = encrypt_encoding(filename)
    print("result1: ", result1)
    print("result1 length: ", len(result1))

    result2 = decode_decrypt(result1)
    print("result2: ", result2)


# test()
