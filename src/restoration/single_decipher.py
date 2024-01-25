import os

import caesar
import background_setting as bg
import decode_base as dba


def build_dictionary(**params):
    result_dict = {key: value for key, value in params.items()}
    return result_dict


def decipher_method(cipher_string):
    result_value1 = caesar.caesar_cipher_decrypt(cipher_string, bg.shift_number)
    print("result_value 1: ", result_value1)

    result_value2 = dba.decoding(result_value1)
    print("result_value 2: ", result_value2)

    return result_value2


def crack_build(absolute_filepath):
    dir_path, file_name = os.path.split(absolute_filepath)
    print("file_name:", file_name, "\ndir_path:", dir_path)

    prepose_folder, parent_dir_name = os.path.split(dir_path)
    print("prepose_folder:", prepose_folder, "\nparent_dir_name:", parent_dir_name)

    real_file_name = decipher_method(file_name)
    real_parent_dir_name = decipher_method(parent_dir_name)

    real_parent_folder = prepose_folder + bg.separator + real_parent_dir_name
    real_absolute_path = real_parent_folder + bg.separator + real_file_name
    transition_filename = dir_path + bg.separator + real_file_name

    result_dict = build_dictionary(
        origin_absolute=absolute_filepath,
        origin_folder=dir_path,
        real_absolute_path=real_absolute_path,
        real_parent_folder=real_parent_folder,
        transition_absolute=transition_filename,
    )
    return result_dict


def test():
    filename = "/linux/amd64/Downloads/7777/777博览会/dVV0T2IzRjRQY2ZPT01uczdPQkxoOFhVejBhQUpFMktvWGJZamZVT29VVT0_e_/ZkkxNlJxVkhSaitmd2dxd0Y1d0pNcUYyMkkzMURxRkY_e_"
    result_dict = crack_build(filename)
    print("result_dict", result_dict)


# test()
