import os
import background_setting as bg
import base_encode as enc
import caesar


def truncate_name(name):
    if len(name) > bg.name_len_limit:
        return name[: bg.name_len_limit]
    else:
        return name


def cropping_file(filepath) -> list:
    folder, file_name = os.path.split(filepath)
    file_name, ext = os.path.splitext(file_name)
    result = [folder, file_name, ext]
    return result


def split_path(path):
    # 使用 os.path.dirname() 获取路径中上层目录
    parent_dir = os.path.dirname(path)
    # 使用 os.path.basename() 获取路径中最后一级目录或文件名
    folder_name = os.path.basename(path)
    return parent_dir, folder_name


def get_new_parent_dir(absolute_path):
    head_directory, folder_name = split_path(absolute_path)

    folder_name = filename_interchange(folder_name)
    truncate_foldername = truncate_name(folder_name)

    new_folder = enc.encoding(truncate_foldername)
    obscure_folder = caesar.caesar_cipher_encrypt(new_folder, bg.shift_number)

    return str(head_directory) + bg.separator + obscure_folder


def filename_interchange(filename):
    for char in bg.redundant_chars:
        filename = filename.replace(char, "")
    filename = filename.replace(" ", ".")
    return filename


def get_new_filename(origin_dir_path, file_title, suffix_name):
    truncate_file_title = truncate_name(file_title)

    filename_encode = enc.encoding(truncate_file_title + suffix_name)
    blur_name = caesar.caesar_cipher_encrypt(filename_encode, bg.shift_number)

    # ENCRYPT
    # blur_name = ofn.encrypt_encoding(blur_name)

    file_name_result = str(origin_dir_path).strip()
    file_name_result += str(bg.separator)
    file_name_result += str(blur_name)

    return file_name_result, blur_name


def build_dictionaries(**params):
    result_dict = {key: value for key, value in params.items()}
    return result_dict


def gain_filename_tuple(filename_list):
    prepose_dirname = filename_list[0]
    regular_filename = filename_list[1]
    suffix_type = filename_list[2]
    return prepose_dirname, regular_filename, suffix_type


def assemble_data(material_file):
    filename_list = cropping_file(material_file)
    prepose_dir, regular_filename, suffix_type = gain_filename_tuple(filename_list)

    new_parent_dir = get_new_parent_dir(prepose_dir)
    file_title = filename_interchange(regular_filename)

    file_update_name, file_new_name = get_new_filename(
        prepose_dir, file_title, suffix_type
    )
    file_new_absolute_path = (
        str(new_parent_dir) + str(bg.separator) + str(file_new_name)
    )

    return build_dictionaries(
        origin_absolute=material_file,
        origin_folder=prepose_dir,
        file_init_title=file_title,
        suffix_name=suffix_type,
        file_new_path=file_update_name,
        new_parent_directory=new_parent_dir,
        new_absolute_path=file_new_absolute_path,
    )
